# -*- coding: utf-8 -*-

from django.urls import path

from eve.vignettes.views import VignetteTypesView, ActiveVignetteView, LicensePlateValidateView, QuickBuyView, BuyView,\
    ExtendView, DelayView, RemoveView, HistoryView

urlpatterns = [
    path("types/<int:vignette_type_id>/edit", VignetteTypesView.as_view()),
    path("types", VignetteTypesView.as_view()),
    path("<str:license_plate>/validate", LicensePlateValidateView.as_view()),
    path("<str:license_plate>/quick-buy", QuickBuyView.as_view()),
    path("<str:license_plate>/buy", BuyView.as_view()),
    path("<str:license_plate>", ActiveVignetteView.as_view()),
    path("<str:vignette_id>/extend", ExtendView.as_view()),
    path("<str:vignette_id>/delay", DelayView.as_view()),
    path("<str:vignette_id>/remove", RemoveView.as_view()),
    path("history", HistoryView.as_view()),
]
