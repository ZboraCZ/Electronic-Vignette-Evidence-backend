# -*- coding: utf-8 -*-

from django.urls import path

from eve.vignettes.views import VignetteTypesView

urlpatterns = [
    path("types", VignetteTypesView.as_view()),
    path("types/<int:vignette_type_id>/edit/", VignetteTypesView.as_view()),
]
