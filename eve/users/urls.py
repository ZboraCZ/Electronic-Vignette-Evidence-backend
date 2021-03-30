# -*- coding: utf-8 -*-

from django.urls import path

from eve.users.views import UsersVignettesView, UsersView

urlpatterns = [
    path("<int:user_id>/vignettes", UsersVignettesView.as_view()),
    path("<int:user_id>", UsersView.as_view()),
]
