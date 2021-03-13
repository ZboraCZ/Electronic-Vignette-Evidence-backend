# -*- coding: utf-8 -*-
"""This module contains database models"""

from django.db import models


class VignetteType(models.Model):
    name = models.CharField(max_length=20)
    display_name = models.CharField(max_length=20)
    price = models.IntegerField()
    duration = models.DurationField()


class Vignette(models.Model):
    vignette_type = models.ForeignKey(VignetteType, on_delete=models.DO_NOTHING)
    serial_number = models.CharField(max_length=25)
    valid_from = models.DateTimeField()
    licence_plate = models.CharField(max_length=8)
