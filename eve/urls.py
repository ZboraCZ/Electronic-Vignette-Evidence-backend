# -*- coding: utf-8 -*-
"""eve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from django.views.generic.base import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("vignettes/", include("eve.vignettes.urls")),
    path("users/", include("eve.users.urls")),
    path("statistics", include("eve.statistics.urls")),
    path("auth/", include("eve.authentication.urls")),
    path("roles/", include("eve.roles.urls")),
    path("swagger-ui/", TemplateView.as_view(template_name='swagger-ui.html'), name="home"),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="api-schema"))
]
