# -*- coding: utf-8 -*-
"""This module contains database operations"""

from .models import VignetteType


def get_all_vignette_types():
    o = VignetteType.objects.all()
    return [vto for vto in VignetteType.objects.all()]