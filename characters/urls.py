from django.urls import path
from . import views

urlpatterns = [
    path("char/", views.CreateListCharacterView.as_view()),
]

