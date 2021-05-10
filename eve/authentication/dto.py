# -*- coding: UTF-8 -*-

from dataclasses import dataclass


@dataclass
class TokenResponse:
    accessToken: str
    userId: int


@dataclass
class AuthErrorResponse:
    error: str
    message: str

