from django.urls import path
from . import views

urlpatterns = [
    path("char/<pk>/attributes/", views.UpdateAttributes.as_view()),
]
