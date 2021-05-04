# -*- coding: utf-8 -*-
"""This module contains database operations"""

from datetime import datetime, timedelta

from django.utils import timezone
from rest_framework.exceptions import NotFound

from .dto import ValidatedVignette
from .models import Vignette, VignetteType


def get_all_vignette_types():
    return [vto for vto in VignetteType.objects.all().order_by("id")]


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


def get_vignette_by_user_id(user):
    vignettes = Vignette.objects.filter(user=user)
    if len(vignettes) > 0:
        return vignettes
    else:
        raise NotFound(detail="User doesn't have any vignette")


def get_actual_and_future_vignettes(license_plate):
    vignettes = list()
    found_vignettes = get_all_vignettes_by_license_plate(license_plate)
    zero = timedelta(0)

    for vignette in found_vignettes:
        days_used = timedelta(days=(timezone.now() - vignette.valid_from).days)
        if vignette.vignette_type.duration >= days_used >= zero:
            vignettes.append(vignette)
        if vignette.valid_from > timezone.now():
            vignettes.append(vignette)
    if vignettes:
        return vignettes
    raise NotFound(detail="Vignette with this license plate doesn't exist")


def get_vignettes_by_license_plate(license_plate):
    try:
        return Vignette.objects.filter(valid_from__lte=datetime.now()).filter(
            license_plate=license_plate
        )
    except Vignette.DoesNotExist:
        raise NotFound(detail="Vignette with this license plate doesn't exist")


def get_all_vignettes_by_license_plate(license_plate):
    return Vignette.objects.filter(license_plate=license_plate)


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


def get_validated_vignette_by_license_plate(license_plate):
    active_vignettes = list()
    not_active_vignettes = list()
    yet_not_active_vignettes = list()
    expired_vignettes = list()

    found_vignettes = get_all_vignettes_by_license_plate(license_plate)
    zero = timedelta(0)

    for vignette in found_vignettes:
        days_used = timedelta(days=(timezone.now() - vignette.valid_from).days)
        if vignette.vignette_type.duration >= days_used >= zero:
            active_vignettes.append(vignette)
        else:
            not_active_vignettes.append(vignette)

    for nav in not_active_vignettes:
        if (timezone.now() - nav.valid_from).days < 0:
            yet_not_active_vignettes.append(nav)
        else:
            expired_vignettes.append(nav)
    yet_not_active_vignettes.sort(key=lambda x: x.valid_from, reverse=True)
    expired_vignettes.sort(key=lambda x: x.valid_from)

    valid = False
    status = ""
    vignette = None
    if active_vignettes:
        valid = True
        status = "active"
        vignette = active_vignettes.pop()
    elif yet_not_active_vignettes:
        status = "not_active"
        vignette = yet_not_active_vignettes.pop()
    elif expired_vignettes:
        status = "expired"
        vignette = expired_vignettes.pop()

    if vignette:
        return ValidatedVignette(
            valid=valid,
            status=status,
            valid_from=vignette.valid_from,
            expire_date=vignette.valid_from + vignette.vignette_type.duration,
        )
    else:
        raise NotFound(
            detail="Vignette with this license plate doesn't exist or is expired"
        )
