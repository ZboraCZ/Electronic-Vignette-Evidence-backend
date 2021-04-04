# -*- coding: utf-8 -*-
"""This module contains database models"""

from datetime import datetime
from eve.roles.models import Roles
from eve.users.models import Users

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)