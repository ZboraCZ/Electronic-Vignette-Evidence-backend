# -*- coding: utf-8 -*-

from django.urls import path

from eve.users.views import UsersLicensePlateView, UsersVignetteHistoryView, UsersDetailView, UsersLookupView

urlpatterns = [
    path("find/<str:user_email>", UsersLookupView.as_view()),
    path("<int:user_id>/licence_plates", UsersLicensePlateView.as_view()),
    path("<int:user_id>/history", UsersVignetteHistoryView.as_view()),
    path("<int:user_id>", UsersDetailView.as_view()),
]
