from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from utils.base_model import UUIDModel

class Drivers(UUIDModel):
    class Meta:
        db_table = 'drivers'


class DriverSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of driver objects."""

    class Meta:
        model = Drivers
        fields = ()