from django.urls import path

from accounts import views

urlpatterns = [
    path("accounts/", views.CreateAccountView.as_view()),
]
