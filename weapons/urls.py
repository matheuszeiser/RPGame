from django.urls import path
from . import views

urlpatterns = [
    path("admin/weapon/", views.WeaponAdminView.as_view()),
    path("admin/weapon/<weapon_id>/", views.WeaponDetailView.as_view())
]