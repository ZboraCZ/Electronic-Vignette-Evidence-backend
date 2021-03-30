# -*- coding: utf-8 -*-

from django.urls import path

from eve.authentication.views import RegistrationView, LoginView, LogoutView

urlpatterns = [
    path("registration", RegistrationView.as_view()),
    path("login", LoginView.as_view()),
    path("logout", LogoutView.as_view()),

]
