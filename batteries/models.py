from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from drivers.models import Drivers

from utils.base_model import UUIDModel

class StatusTypes(models.TextChoices):
    ACTIVE = 'ACTIVE', _('ACTIVE')
    INACTIVE = 'INACTIVE', _('INACTIVE')
    CHARGED = 'CHARGED', _('CHARGED')
    CHARGING = 'CHARGING', _('CHARGING')

class Batteries(UUIDModel):
    serial = models.CharField(max_length=100, null=True, unique=True)
    state_of_health = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    state_of_charge = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    status = status = models.CharField(
        max_length=50,
        choices=StatusTypes.choices,
        default=StatusTypes.ACTIVE,
    )

    class Meta:
        db_table = 'batteries'

class BatteryTelematics(UUIDModel):
    current_charge = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    longitude = models.CharField(max_length=100, null=True)
    latitude = models.CharField(max_length=100, null=True)
    battery = models.ForeignKey(
        Batteries,
        on_delete=models.PROTECT,
        null=True
    )
    driver = models.ForeignKey(
        Drivers,
        on_delete=models.PROTECT,
        null=True
    )

    class Meta:
        db_table = 'battery_telematics'

class BatterySerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Battery objects."""

    class Meta:
        model = Batteries
        fields = (
            'id',
            'serial',
            'state_of_charge',
            'state_of_health',
            'status'
        )