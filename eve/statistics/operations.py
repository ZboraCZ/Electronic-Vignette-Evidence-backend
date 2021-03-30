# -*- coding: utf-8 -*-
"""This module contains database operations"""

from rest_framework.exceptions import NotFound

from .models import Statistics


def get_statistics():
    try:
        return Statistics.objects.all().last()
    except Statistics.DoesNotExist:
        raise NotFound(detail="Statistics Not Found")
