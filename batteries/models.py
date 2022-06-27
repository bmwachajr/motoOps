from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from utils.base_model import UUIDModel

class Batteries(UUIDModel):
    class Meta:
        db_table = 'batteries'


class BatterySerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Battery objects."""

    class Meta:
        model = Batteries
        fields = ()