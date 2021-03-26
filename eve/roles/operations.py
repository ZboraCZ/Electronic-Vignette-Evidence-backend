# -*- coding: utf-8 -*-
"""This module contains database operations"""

from rest_framework.exceptions import NotFound

from eve.roles.models import Roles


def get_all_roles():
    try:
        return [ro for ro in Roles.objects.all()]
    except Roles.DoesNotExist:
        raise NotFound(detail="Roles Not Found")
