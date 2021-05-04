# -*- coding: utf-8 -*-

from django.urls import include, path
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.reverse import reverse_lazy

urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy("api-schema-swagger"))),
    path("vignettes/", include("eve.vignettes.urls")),
    path("users/", include("eve.users.urls")),
    path("statistics", include("eve.statistics.urls")),
    path("auth/", include("eve.authentication.urls")),
    path("roles/", include("eve.roles.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-schema-swagger",
    ),
]
