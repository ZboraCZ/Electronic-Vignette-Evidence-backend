# -*- coding: utf-8 -*-
"""This module contains database operations"""
from rest_framework.exceptions import NotFound
from rest_framework.authtoken.models import Token

from eve.exceptions import UserCheckFailed


def check_user(request, user_id):
    token = request.user.auth_token
    id_token = Token.objects.get(key=token).user_id
    if id_token == user_id or request.user.role_id == 1:
        return
    raise UserCheckFailed()
