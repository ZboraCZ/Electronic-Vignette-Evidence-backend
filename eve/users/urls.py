# -*- coding: utf-8 -*-

from django.urls import path

from eve.users.views import UsersView

urlpatterns = [
    path("<int:user_id>", UsersView.as_view()),
    path("<int:user_id/vignettes>", UsersView.as_view()),
    path("<int:user_id/vignettes/edit>", UsersView.as_view()),
]