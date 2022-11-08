from django.urls import path

from armors import views

urlpatterns = [
    path("armor/<armor_id>/", views.ListArmorView.as_view()),
    path("armors/", views.ListArmorsView.as_view()),
    path("admin/armor/", views.CreateArmorView.as_view()),
    path("admin/armor/<armor_id>/", views.ArmorDetailView.as_view()),
]
