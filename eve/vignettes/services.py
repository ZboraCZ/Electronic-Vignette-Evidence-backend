# -*- coding: utf-8 -*-
"""This module contains business logic"""

from .models import Vignette


def create_new_vignette(user, vignette_type, valid_from, license_plate):
    Vignette(user=user, vignette_type=vignette_type, serial_number="0", valid_from=valid_from,
             license_plate=license_plate).save()


def create_new_vignette_quick(vignette_type, valid_from, license_plate):
    Vignette(vignette_type=vignette_type, serial_number="0", valid_from=valid_from, license_plate=license_plate).save()


def extend_vignette(vignette, vignette_type, valid_from):
    vignette.vignette_type = vignette_type
    vignette.valid_from = valid_from
    vignette.save()


def delay_vignette(vignette, valid_from):
    vignette.valid_from = valid_from
    vignette.save()