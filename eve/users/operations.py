# -*- coding: utf-8 -*-
"""This module contains database operations"""

from rest_framework.exceptions import NotFound

from .dto import LicencePlate
from .models import Users

from eve.vignettes.operations import get_vignette_by_user_id, get_all_vignettes_by_license_plate


def _get_license_plates_by_user(user_id):
    vignettes = get_vignette_by_user_id(get_one_user(user_id))
    license_plate = list()
    for vignette in vignettes:
        license_plate.append(vignette.license_plate)

    return set(license_plate)


def get_one_user(user_id):
    try:
        return Users.objects.get(id=user_id)
    except Users.DoesNotExist:
        raise NotFound(detail="User Not Found")


def get_user_by_email(user_email):
    try:
        return Users.objects.get(email=user_email)
    except Users.DoesNotExist:
        raise NotFound(detail="User Not Found")


def get_users_licence_plates(user_id):
    return [
        LicencePlate(lp) for lp in _get_license_plates_by_user(user_id)
    ]


def get_users_history(user_id):
    vignettes_history = []
    try:
        licence_plates = _get_license_plates_by_user(user_id)
    except NotFound:
        licence_plates = []

    for lp in licence_plates:
        lp_vignettes = get_all_vignettes_by_license_plate(lp)
        vignettes_history.extend(lp_vignettes)

    return vignettes_history
