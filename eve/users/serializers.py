# -*- coding: utf-8 -*-
"""This module contains JSON response serializers"""

from rest_framework import serializers

from .models import Users
from eve.roles.serializers import RoleSerializer

class UsersSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)

    class Meta:
        model = Users
        fields = ["id", "role", "email", "first_name", "last_name", "phone", "password"]
