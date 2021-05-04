# -*- coding: utf-8 -*-
"""This module contains database models"""
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.db import models

from eve.roles.models import Roles
from eve.users.validators import name_regex, phone_regex


class Users(AbstractBaseUser):
    role = models.ForeignKey(
        Roles, on_delete=models.DO_NOTHING, default=2  # default=2 is User role
    )
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(validators=[name_regex], max_length=50)
    last_name = models.CharField(validators=[name_regex], max_length=50)
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    password = models.CharField(max_length=64)
    REQUIRED_FIELDS = ["password"]
    USERNAME_FIELD = "email"
