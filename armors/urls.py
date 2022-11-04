from django.urls import path

from armors import views

urlpatterns = [
    path("admin/armor/", views.CreateListArmorView.as_view()),
    path("admin/armor/<pk>/", views.ArmorDetailView.as_view()),
]
