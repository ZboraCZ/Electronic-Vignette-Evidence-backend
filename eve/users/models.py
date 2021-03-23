# -*- coding: utf-8 -*-
"""This module contains database models"""

from django.db import models

class Users(models.Model):
    email = models.CharField(max_length=320)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
