# -*- coding: utf-8 -*-
"""This module contains database operations"""

from rest_framework.exceptions import NotFound

from .models import VignetteType, Vignette

from datetime import datetime, timedelta
from django.utils import timezone


def get_all_vignette_types():
    return [vto for vto in VignetteType.objects.all().order_by('id')]


def get_one_vignette_type(vignette_id):
    try:
        return VignetteType.objects.get(id=vignette_id)
    except VignetteType.DoesNotExist:
        raise NotFound(detail="Vignette Type Not Found")


def get_vignettes_by_license_plate(license_plate):
    try:
        return Vignette.objects.filter(valid_from__lte=datetime.now()).filter(license_plate=license_plate)
    except Vignette.DoesNotExist:
        raise NotFound(detail="Vignette with this license plate doesn't exist")


def get_active_vignette_by_license_plate(license_plate):
    now = timezone.now()
    valid_vignettes = []
    found_vignettes = get_vignettes_by_license_plate(license_plate)

    for vignette in found_vignettes:
        days_used = timedelta(days=(now-vignette.valid_from).days)

        if days_used <= vignette.vignette_type.duration:
            valid_vignettes.append(vignette)

    if len(valid_vignettes) > 0:
        return valid_vignettes
    else:
        raise NotFound(detail="Vignette with this license plate doesn't exist.")
