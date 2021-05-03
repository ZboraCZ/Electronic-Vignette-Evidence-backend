# -*- coding: utf-8 -*-
"""This module contains database operations"""

from rest_framework.exceptions import NotFound

from .models import VignetteType, Vignette

from datetime import datetime, timedelta
from django.utils import timezone

from dataclasses import dataclass


@dataclass
class ValidatedVignette:
    valid: bool
    valid_from: datetime
    expire_date: datetime


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


def get_vignette_by_user_id(user):
    vignettes = []
    vignettes = Vignette.objects.filter(user=user)
    if len(vignettes) > 0:
        return vignettes
    else:
        raise NotFound(detail="User doesn't have any vignette")


def get_vignettes_by_license_plate(license_plate):
    try:
        return Vignette.objects.filter(valid_from__lte=datetime.now()).filter(license_plate=license_plate)
    except Vignette.DoesNotExist:
        raise NotFound(detail="Vignette with this license plate doesn't exist")


def get_all_vignettes_by_license_plate(license_plate):
    all_vignette = []
    try:
        found_vignettes = Vignette.objects.filter(license_plate=license_plate)
        for vignette in found_vignettes:
            all_vignette.append(vignette)
        return all_vignette
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


def get_validated_vignette_by_license_plate(license_plate):
    valid_vignettes = []
    not_active_yet_vignettes = []
    expired_vignettes = []

    active_vignettes = get_active_vignette_by_license_plate(license_plate)
    all_vignettes = get_all_vignettes_by_license_plate(license_plate)
    not_active_vignettes = set(all_vignettes) - set(active_vignettes)

    for active_vignette in active_vignettes:
        validated_vignette = ValidatedVignette(valid=True, valid_from=active_vignette.valid_from)
        valid_vignettes.append(validated_vignette)
    for not_active_vignette in not_active_vignettes:
        if (timezone.now() - not_active_vignette.valid_from).days < 0:
            not_active_yet_vignettes.append(ValidatedVignette(valid=False, valid_from=not_active_vignette.valid_from))
        else:
            expired_vignettes.append(ValidatedVignette(valid=False, valid_from=not_active_vignette.valid_from))

    if len(valid_vignettes) > 0:
        vignette = valid_vignettes.pop()
        status = True
        valid_from = vignette.valid_from
        expire_date = vignette.expire_date
    elif len(not_active_yet_vignettes) > 0:
        not_active_yet_vignettes.sort(key=lambda x: x.valid_from, reverse=True)
        vignette = not_active_yet_vignettes.pop()
        status = False
        valid_from = vignette.valid_from
        expire_date = vignette.expire_date
    elif len(expired_vignettes) > 0:
        expired_vignettes.sort(key=lambda x: x.valid_from, reverse=False)
        vignette = expired_vignettes.pop()
        status = False
        valid_from = vignette.valid_from
        expire_date = vignette.expire_date
    else:
        status = False
        valid_from = ""
        expire_date = ""

    if len(valid_vignettes) > 0 or len(not_active_vignettes) > 0 or len(expired_vignettes) > 0:
        return ValidatedVignette(valid=status, valid_from=valid_from, expire_date=expire_date)
    else:
        raise NotFound(detail="Vignette with this license plate doesn't exist or is expired")


def get_if_vignette_already_bought_by_license_plate(license_plate):
    now = timezone.now()
    found_vignettes = get_vignettes_by_license_plate(license_plate)
    valid_vignettes = []

    for vignette in found_vignettes:
        days_used = timedelta(days=(now - vignette.valid_from).days)

        if days_used <= vignette.vignette_type.duration:
            valid_vignettes.append(vignette)

    if len(valid_vignettes) == 0:
        return valid_vignettes
    else:
        raise NotFound("Vignette with this license vignette already bought and valid.")




