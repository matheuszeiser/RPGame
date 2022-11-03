from django.urls import path
from . import views

urlpatterns = [
    path("char/<pk>/inventory/", views.RetrieveInventoryView.as_view()),
]
