from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from utils.base_model import UUIDModel

class Swaps(UUIDModel):
    class Meta:
        db_table = 'swaps'


class SwapSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Swap objects."""

    class Meta:
        model = Swaps
        fields = ()