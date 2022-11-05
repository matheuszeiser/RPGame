from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from accounts import views

urlpatterns = [
    path("accounts/", views.CreateAccountView.as_view()),
    path("accounts/login/", ObtainAuthToken.as_view()),
    path("accounts/<pk>/", views.RetrieveUpdateDestroyView.as_view()),
    path("admin/accounts/", views.AdminListAccountsView.as_view()),
    path(
        "admin/accounts/<pk>/",
        views.AdminActivateDeleteAccountView.as_view(),
    ),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
