# -*- coding: utf-8 -*-
"""This module contains database models"""
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from eve.roles.models import Roles


class Users(AbstractBaseUser):
    role = models.ForeignKey(
        Roles, on_delete=models.DO_NOTHING, default=2  # default=2 is User role
    )
    email = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    REQUIRED_FIELDS = ["password_hash", "first_name", "phone"]
    USERNAME_FIELD = "email"
