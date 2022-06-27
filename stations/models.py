from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from utils.base_model import UUIDModel

class StatusTypes(models.TextChoices):
    ACTIVE = 'ACTIVE', _('ACTIVE')
    INACTIVE = 'INACTIVE', _('INACTIVE')

class Stations(UUIDModel):
    name = models.CharField(max_length=10, null=True)
    longitude = models.CharField(max_length=100, null=True)
    latitude = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    status = status = models.CharField(
        max_length=50,
        choices=StatusTypes.choices,
        default=StatusTypes.ACTIVE,
    )
    class Meta:
        db_table = 'stations'


class StationSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Station objects."""

    class Meta:
        model = Stations
        fields = (
            'id',
            'name',
            'longitude',
            'latitude',
            'contact',
            'status'
        )