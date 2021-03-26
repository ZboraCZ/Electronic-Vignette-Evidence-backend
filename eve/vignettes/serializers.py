# -*- coding: utf-8 -*-
"""This module contains JSON response serializers"""

from rest_framework import serializers

from .models import VignetteType, Vignette


class VignetteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VignetteType
        fields = ["id", "name", "display_name", "price", "duration"]

class VignetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vignette
        fields = ["id", "id_user", "id_vignette_type", "serial_number", "valid_from", "license_plate"]
