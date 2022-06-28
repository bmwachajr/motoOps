from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from utils.base_model import UUIDModel

class StatusTypes(models.TextChoices):
    ACTIVE = 'ACTIVE', _('ACTIVE')
    INACTIVE = 'INACTIVE', _('INACTIVE')

class Drivers(UUIDModel):
    fullname = models.CharField(max_length=100, null=True, unique=False)
    emoto_license = models.CharField(max_length=10, null=True, unique=True)
    contact = models.CharField(max_length=15, null=False, unique=True, default='')
    energy_consumption_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True) # measured in Kwh/Mile
    status = status = models.CharField(
        max_length=50,
        choices=StatusTypes.choices,
        default=StatusTypes.ACTIVE,
    )

    def get_energy_consumed(self, distance):
        """compute the energy consumed in KWH by an emoto given distance traveled in miles"""
        energy_consumed = self.energy_consumption_rate * distance
        return Decimal(energy_consumed)

    def get_distance_traveled(self, energy_consumed):
        """compute the distance in miles traveled by an emoto given energy consumed traveled in KiloWatt Hour"""
        return energy_consumed / self.energy_consumption_rate

    class Meta:
        db_table = 'drivers'


class DriverSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of driver objects."""

    class Meta:
        model = Drivers
        fields = (
            'id',
            'fullname',
            'emoto_license',
            'contact',
            'energy_consumption_rate',
            'status'
        )