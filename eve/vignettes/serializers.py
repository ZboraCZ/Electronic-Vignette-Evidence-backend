# -*- coding: utf-8 -*-
"""This module contains JSON response serializers"""

from rest_framework import serializers

from .models import Vignette, VignetteType


class VignetteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VignetteType
        fields = ["id", "name", "display_name", "price", "duration"]


class VignetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vignette
        fields = [
            "id",
            "user_id",
            "vignette_type_id",
            "serial_number",
            "valid_from",
            "license_plate",
            "created",
        ]


class ValidatedVignetteSerializer(serializers.Serializer):
    valid = serializers.BooleanField()
    status = serializers.CharField()
    valid_from = serializers.DateTimeField()
    expire_date = serializers.DateTimeField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class QuickBuyVignetteSerializer(serializers.Serializer):
    id_vignette_type = serializers.IntegerField()
    valid_from = serializers.DateTimeField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class BuyVignetteSerializer(serializers.Serializer):
    id_vignette_type = serializers.IntegerField()
    id_user = serializers.IntegerField()
    valid_from = serializers.DateTimeField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class ExtendVignetteSerializer(serializers.Serializer):
    days = serializers.IntegerField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class DelayVignetteSerializer(serializers.Serializer):
    delay_date = serializers.DateTimeField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
