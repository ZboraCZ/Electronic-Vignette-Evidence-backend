# -*- coding: utf-8 -*-
"""This module contains database models"""

from django.db import models


class Roles(models.Model):
    name = models.CharField(max_length=25)

