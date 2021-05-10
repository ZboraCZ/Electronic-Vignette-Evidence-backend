# -*- coding: utf-8 -*-

from django.urls import path

from eve.authentication.views import LoginView, RegistrationView

urlpatterns = [
    path("registration", RegistrationView.as_view()),
    path("login", LoginView.as_view()),
]
