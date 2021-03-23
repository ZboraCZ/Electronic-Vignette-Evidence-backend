# -*- coding: utf-8 -*-
"""This module contains JSON response serializers"""

from rest_framework import serializers

from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id", "email", "first_name", "last_name", "phone"]