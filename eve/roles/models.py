# -*- coding: utf-8 -*-
"""This module contains database models"""

from django.db import models


class Roles(models.Model):
    ADMIN = 1
    USER = 2

    ROLE_NAME_CHOICES = [
        (ADMIN, 'admin'),
        (USER, 'user'),
    ]

    name = models.CharField(max_length=25,
                            choices=ROLE_NAME_CHOICES,
                            default=USER
                            )
