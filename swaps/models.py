from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from batteries.models import Batteries, BatterySerializer
from drivers.models import DriverSerializer, Drivers
from stations.models import StationSerializer, Stations

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
    status = status = models.CharField(
        max_length=50,
        choices=StatusTypes.choices,
        default=StatusTypes.PENDING,
    )

    class Meta:
        db_table = 'swaps'


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