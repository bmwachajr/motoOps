from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from utils.base_model import UUIDModel

class Stations(UUIDModel):
    class Meta:
        db_table = 'stations'


class StationSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Station objects."""

    class Meta:
        model = Stations
        fields = ()