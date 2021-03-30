# -*- coding: utf-8 -*-

from django.urls import path

from eve.roles.views import RolesView
from eve.statistics.views import StatisticsView

urlpatterns = [
    path("", StatisticsView.as_view()),
]
