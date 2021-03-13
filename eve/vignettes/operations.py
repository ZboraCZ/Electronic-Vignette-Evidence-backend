# -*- coding: utf-8 -*-
"""This module contains database operations"""

from .models import VignetteType
from rest_framework.exceptions import NotFound


def get_all_vignette_types():
    o = VignetteType.objects.all()
    return [vto for vto in VignetteType.objects.all()]

def get_one_vignette_type(vId):
    try:
        return VignetteType.objects.get(id=vId)
    except VignetteType.DoesNotExist:
        raise NotFound(detail="Vignette Not Found")
