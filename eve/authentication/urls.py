# -*- coding: utf-8 -*-

from django.urls import path

from eve.authentication.views import RegistrationView, LoginView

urlpatterns = [
    path("registration", RegistrationView.as_view()),
    path("login", LoginView.as_view()),
]
