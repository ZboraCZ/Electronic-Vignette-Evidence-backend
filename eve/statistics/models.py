# -*- coding: utf-8 -*-
"""This module contains database models"""

from django.db import models


class Statistics(models.Model):
    active = models.IntegerField()
    sold = models.IntegerField()
    valid = models.IntegerField()
    invalid = models.IntegerField()
    generated = models.DateTimeField()

