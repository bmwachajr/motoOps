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
    status = status = models.CharField(
        max_length=50,
        choices=StatusTypes.choices,
        default=StatusTypes.ACTIVE,
    )

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
            'status'
        )