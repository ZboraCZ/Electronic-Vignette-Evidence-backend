# -*- coding: utf-8 -*-
"""This module contains database models"""

from django.db import models

from eve.roles.models import Roles


class Users(models.Model):

    role = models.ForeignKey(
        Roles, on_delete=models.DO_NOTHING, default=2  # default=2 is User role
    )

    #role = models.OneToOneField(Roles, on_delete=models.DO_NOTHING, default=2)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=64)
    phone = models.CharField(max_length=15)
