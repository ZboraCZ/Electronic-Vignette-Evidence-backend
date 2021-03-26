# -*- coding: utf-8 -*-

from django.urls import path

from eve.vignettes.views import VignetteTypesView, VignettesView

urlpatterns = [
    path("types", VignetteTypesView.as_view()),
    path("types/<int:vignette_type_id>/edit", VignetteTypesView.as_view()),
    path("<str:license_plate>", VignettesView.as_view()),
]
