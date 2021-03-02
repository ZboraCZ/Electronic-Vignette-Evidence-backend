# -*- coding: utf-8 -*-

from django.urls import path

from eve.vignette.views import VignetteDetailsView

urlpatterns = [
    path("", VignetteDetailsView.as_view()),
]
