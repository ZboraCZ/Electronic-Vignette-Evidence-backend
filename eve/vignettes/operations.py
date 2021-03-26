# -*- coding: utf-8 -*-
"""This module contains database operations"""

from rest_framework.exceptions import NotFound

from .models import VignetteType, Vignette

from datetime import datetime, timedelta


def get_all_vignette_types():
    return [vto for vto in VignetteType.objects.all()]


def get_one_vignette_type(vignette_id):
    try:
        return VignetteType.objects.get(id=vignette_id)
    except VignetteType.DoesNotExist:
        raise NotFound(detail="Vignette Not Found")


def get_active_vignette_by_license_plate(license_plate):
    try:
        validVignette = Vignette.objects.filter(idVignetteType__valid_from < datetime.now())
        print(validVignette)
        return Vignette.objects.get(id=vignette_id)
    except VignetteType.DoesNotExist:
        raise NotFound(detail="Vignette Not Found")
