# -*- coding: utf-8 -*-
"""This module contains database operations"""
from rest_framework.exceptions import NotFound
from rest_framework.authtoken.models import Token

from eve.authentication.dto import TokenResponse, AuthErrorResponse
from eve.exceptions import UserCheckFailed
from eve.utils import encrypt_string


def check_user(request, user_id):
    token = request.user.auth_token
    id_token = Token.objects.get(key=token).user_id
    if id_token == user_id or request.user.role_id == 1:
        return
    raise UserCheckFailed()


def generate_token_response(user):
    token = Token.objects.get(user=user).key
    return TokenResponse(
        accessToken=token,
        userId=user.id
    )


def generate_email_response():
    return AuthErrorResponse(
        error="AUTH_ERROR",
        message="wrong email"
    )


def generate_password_response():
    return AuthErrorResponse(
        error="AUTH_ERROR",
        message="wrong password"
    )


def encrypt_password_in_dict(data):
    password_hash = encrypt_string(data["password"])
    data["password"] = password_hash
    return data

