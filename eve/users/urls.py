# -*- coding: utf-8 -*-

from django.urls import path

from eve.users.views import UsersLicensePlateView, UsersVignetteHistoryView, UsersView

urlpatterns = [
    path("<int:user_id>/licence_plates", UsersLicensePlateView.as_view()),
    path("<int:user_id>/history", UsersVignetteHistoryView.as_view()),
    path("<int:user_id>", UsersView.as_view()),
]
