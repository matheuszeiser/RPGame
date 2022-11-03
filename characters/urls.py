from django.urls import path
from . import views

urlpatterns = [
    path("char/", views.CreateListCharacterView.as_view()),
    path("char/<pk>/", views.RetrieveUpdateDeleteCharView.as_view()),
]
