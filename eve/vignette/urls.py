# -*- coding: utf-8 -*-

from django.urls import path

from eve.vignette.views import VignetteTypesView

urlpatterns = [
    path("types", VignetteTypesView.as_view()),
]
