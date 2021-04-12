# -*- coding: utf-8 -*-
"""This module contains database operations"""

from rest_framework.exceptions import NotFound

from .models import VignetteType, Vignette, ValidatedVignette

from datetime import datetime, timedelta
from django.utils import timezone


def get_all_vignette_types():
    return [vto for vto in VignetteType.objects.all().order_by('id')]


def get_one_vignette_type(vignette_id):
    try:
        return VignetteType.objects.get(id=vignette_id)
    except VignetteType.DoesNotExist:
        raise NotFound(detail="Vignette Type Not Found")


def get_one_vignette_by_id(vignette_id):
    try:
        return Vignette.objects.get(id=vignette_id)
    except Vignette.DoesNotExist:
        raise NotFound(detail="Vignette not found")


def get_vignettes_by_license_plate(license_plate):
    try:
        return Vignette.objects.filter(valid_from__lte=datetime.now()).filter(license_plate=license_plate)
    except Vignette.DoesNotExist:
        raise NotFound(detail="Vignette with this license plate doesn't exist")


def get_all_vignettes_by_licence_plate(licence_plate):
    try:
        return Vignette.objects.filter(licence_plate=licence_plate)
    except Vignette.DoesNotExist:
        raise NotFound(detail="Vignette with this license plate doesn't exist")


def get_active_vignette_by_license_plate(license_plate):
    now = timezone.now()
    valid_vignettes = []
    found_vignettes = get_vignettes_by_license_plate(license_plate)

    for vignette in found_vignettes:
        days_used = timedelta(days=(now - vignette.valid_from).days)

        if days_used <= vignette.vignette_type.duration:
            valid_vignettes.append(vignette)

    if len(valid_vignettes) > 0:
        return valid_vignettes
    else:
        raise NotFound(detail="Vignette with this license plate doesn't exist.")


def get_expired_vignette_by_license_plate(licence_plate):
    now = timezone.now()
    expired_vignettes = []
    found_vignettes = get_vignettes_by_license_plate(licence_plate)

    for vignette in found_vignettes:
        days_used = timedelta(days=(now))


def get_validated_vignette_by_license_plate(license_plate):
    validated_vignettes = []

    active_vignettes = get_active_vignette_by_license_plate(license_plate)
    all_vignettes = get_all_vignettes_by_licence_plate(license_plate)
    expired_vignettes = all_vignettes - active_vignettes

    for active_vignette in active_vignettes:
        validated_vignette = ValidatedVignette(valid=True, vignette=active_vignette)
        validated_vignettes.append(validated_vignette)
    for expired_vignette in expired_vignettes:
        validated_vignette = ValidatedVignette(valid=False, vignette=expired_vignette)
        validated_vignettes.append(validated_vignette)

    if len(validated_vignettes) > 0:
        return validated_vignettes
    else:
        raise NotFound(detail="Vignette with this licence plate doesn't exist")






