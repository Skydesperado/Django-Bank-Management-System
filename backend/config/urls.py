import os

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path(os.environ.get("ADMIN_PANEL_URL"), admin.site.urls),
    path("customer/", include("apps.customer.apis.urls")),
    path("account/", include("apps.account.apis.urls")),
    path("transaction/", include("apps.transaction.apis.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema")),
        path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema")),
    ]
