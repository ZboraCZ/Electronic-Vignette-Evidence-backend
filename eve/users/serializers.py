# -*- coding: utf-8 -*-
"""This module contains JSON response serializers"""
from django.core.validators import RegexValidator
from rest_framework import serializers

from .models import Users
from eve.roles.serializers import RoleSerializer
from .validators import name_regex, phone_regex
from ..utils import encrypt_string


class UsersAuthSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)

    class Meta:
        model = Users
        fields = ["id", "role", "email", "first_name", "last_name", "phone", "password"]


class UsersSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)

    class Meta:
        model = Users
        fields = ["id", "role", "email", "first_name", "last_name", "phone"]


class LicensePlateSerializer(serializers.Serializer):
    license_plate = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class EditUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    first_name = serializers.CharField(validators=[name_regex], max_length=50)
    last_name = serializers.CharField(validators=[name_regex], max_length=50)
    phone = serializers.CharField(validators=[phone_regex], max_length=17)
    password = serializers.CharField(max_length=64, required=False)

    class Meta:
        validators = []

    def update(self, instance, validated_data):
        instance.first_name = validated_data["first_name"]
        instance.last_name = validated_data["first_name"]
        instance.phone = validated_data["phone"]
        if "password" in validated_data:
            new_password = encrypt_string(validated_data["password"])
            instance.password = new_password
        instance.save()