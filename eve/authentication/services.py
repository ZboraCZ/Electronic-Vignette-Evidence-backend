# -*- coding: utf-8 -*-
"""This module contains business logic"""

from eve.authentication.dto import AuthErrorResponse
from eve.utils import encrypt_string


def generate_email_response():
    return AuthErrorResponse(error="AUTH_ERROR", message="wrong email")


def generate_password_response():
    return AuthErrorResponse(error="AUTH_ERROR", message="wrong password")


def encrypt_password_in_dict(data):
    password_hash = encrypt_string(data["password"])
    data["password"] = password_hash
    return data
