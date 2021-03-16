# -*- coding: utf-8 -*-
"""This module contains JSON response serializers"""

from rest_framework import serializers

from .models import VignetteType


class VignetteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VignetteType
        fields = ["id", "name", "display_name", "price", "duration"]
