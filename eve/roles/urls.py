# -*- coding: utf-8 -*-

from django.urls import path

from eve.roles.views import RolesView

urlpatterns = [
    path("", RolesView.as_view()),
]
