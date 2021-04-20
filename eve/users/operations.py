# -*- coding: utf-8 -*-
"""This module contains database operations"""

from .models import Users
from rest_framework.exceptions import NotFound
from eve.vignettes.operations import get_vignette_by_user_id


def get_one_user(user_id):
    try:
        return Users.objects.get(id=user_id)
    except Users.DoesNotExist:
        raise NotFound(detail="User Not Found")


def get_users_license_plate(user_id):
    vignettes = get_vignette_by_user_id(get_one_user(user_id))
    license_plate = []
    for vignette in vignettes:
        license_plate.append({"license_plate": vignette.license_plate})

    return license_plate
