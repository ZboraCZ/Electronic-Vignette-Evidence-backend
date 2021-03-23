# -*- coding: utf-8 -*-
"""This module contains database operations"""

from .models import Users
from rest_framework.exceptions import NotFound


def get_one_user(uId):
    try:
        return Users.objects.get(id=uId)
    except Users.DoesNotExist:
        raise NotFound(detail="User Not Found")
