# -*- coding: utf-8 -*-
"""This module contains JSON response serializers"""

from rest_framework import serializers

from eve.users.models import Users


class AuthUsersSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


class TokenSerializer(serializers.Serializer):
    key = serializers.CharField()