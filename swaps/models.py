from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from batteries.models import Batteries, BatterySerializer, BatteryTelematics
from drivers.models import DriverSerializer, Drivers
from stations.models import StationSerializer, Stations

from django.db.models import signals
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from utils.base_model import UUIDModel

class StatusTypes(models.TextChoices):
    INPROGRESS = 'INPROGRESS', _('INPROGRESS')
    CANCELLED = 'CANCELLED', _('Cancelled')
    PENDING = 'PENDING', _('Pending')
    COMPLETED = 'COMPLETED', _('Completed')

class Swaps(UUIDModel):
    battery_swapped_in = models.ForeignKey(
        Batteries,
        related_name='battery_swapped_in',
        on_delete=models.PROTECT,
        null=True
    )
    battery_swapped_out = models.ForeignKey(
        Batteries,
        related_name='battery_swapped_out',
        on_delete=models.PROTECT,
        null=True
    )
    driver = models.ForeignKey(
        Drivers,
        related_name='driver',
        on_delete=models.PROTECT,
        null=True
    )
    station = models.ForeignKey(
        Stations,
        related_name='station',
        on_delete=models.PROTECT,
        null=True
    )
    charge_used = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    amount_payable = models.DecimalField(max_digits=25, decimal_places=2, null=True)
    distance_traveled = models.DecimalField(max_digits=25, decimal_places=2, null=True)
    status = status = models.CharField(
        max_length=50,
        choices=StatusTypes.choices,
        default=StatusTypes.PENDING,
    )

    def save(self, *args, **kwargs):
        # get the current charge from the batteries telematic records and subtracts it from the net capacity of the battery
        self.charge_used = self.set_charge_used()

        #assume each unit of energy costs 2 cents
        self.amount_payable = Decimal(0.2) * self.charge_used

        # Find distance traveled by dividving charge used by the energy consumption of a driver
        self.distance_traveled = self.charge_used / self.driver.energy_consumption_rate

        super().save(*args, **kwargs)

    def set_charge_used(self):
        latest_telematic = BatteryTelematics.objects.filter(
                battery=self.battery_swapped_out
                    ).first()

        return self.battery_swapped_out.net_capacity - latest_telematic.current_charge if latest_telematic else Decimal(0)

    class Meta:
        db_table = 'swaps'

@receiver(post_save, sender=Swaps)
def receiver(instance, created, *args, **kwargs):
    if created:
        instance.battery_swapped_in.status = 'ACTIVE'
        instance.battery_swapped_out.status = 'INACTIVE'

class SwapSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Swap objects."""
    battery_swapped_in = BatterySerializer(many=False)
    battery_swapped_out = BatterySerializer(many=False)
    driver  = DriverSerializer(many=False)
    station = StationSerializer(many=False)

    class Meta:
        model = Swaps
        fields = (
            'id',
            'battery_swapped_in',
            'battery_swapped_out',
            'driver',
            'station',
            'charge_used',
            'amount_payable',
            'distance_traveled',
            'status'
        )


class PostSwapSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Swap objects."""
    class Meta:
        model = Swaps
        fields = (
            'id',
            'battery_swapped_in',
            'battery_swapped_out',
            'driver',
            'station',
            'charge_used',
            'amount_payable',
            'status'
        )