# -*- coding: utf-8 -*-
"""This module contains business logic"""

from datetime import datetime, timedelta

from django.utils import timezone

from ..exceptions import AfterStartDate, AlreadyEdited, MaxDaysExceeded
from .models import Vignette


def create_new_vignette(user, vignette_type, valid_from, license_plate):
    Vignette(
        user=user,
        vignette_type=vignette_type,
        serial_number="0",
        valid_from=valid_from,
        license_plate=license_plate,
        created=timezone.now(),
    ).save()


def create_new_vignette_quick(vignette_type, valid_from, license_plate):
    Vignette(
        vignette_type=vignette_type,
        serial_number="0",
        valid_from=valid_from,
        license_plate=license_plate,
        created=timezone.now(),
    ).save()


def extend_vignette(vignette, vignette_type, valid_from):
    vignette.vignette_type = vignette_type
    vignette.valid_from = valid_from
    vignette.save()


def str_to_timezone(time_str):
    date_format = "%Y-%m-%dT%H:%M:%S%z"
    return datetime.strptime(time_str, date_format)


def delay_vignette(vignette, valid_from):
    if vignette.edited:
        raise AlreadyEdited()
    if vignette.valid_from < timezone.now():
        raise AfterStartDate()
    if str_to_timezone(valid_from) > (vignette.valid_from + timedelta(days=90)):
        raise MaxDaysExceeded()
    vignette.valid_from = valid_from
    vignette.edited = True
    vignette.save()
