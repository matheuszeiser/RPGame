from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from accounts import views

urlpatterns = [
    path("accounts/", views.CreateAccountView.as_view()),
    path("accounts/login/", ObtainAuthToken.as_view()),
    path("accounts/<pk>/", views.RetrieveUpdateDestroyView.as_view()),
]
