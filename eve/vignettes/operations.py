# -*- coding: utf-8 -*-
"""This module contains database operations"""

from rest_framework.exceptions import NotFound

from .models import VignetteType


def get_all_vignette_types():
    return [vto for vto in VignetteType.objects.all()]


def get_one_vignette_type(vignette_id):
    try:
        return VignetteType.objects.get(id=vignette_id)
    except VignetteType.DoesNotExist:
        raise NotFound(detail="Vignette Not Found")
