from django.urls import path
from . import views

urlpatterns = [
    path("weapon/<weapon_id>/", views.WeaponListView.as_view()),
    path("weapons/", views.WeaponsListView.as_view()),
    path("admin/weapon/", views.WeaponAdminView.as_view()),
    path("admin/weapon/<weapon_id>/", views.WeaponDetailView.as_view()),
]
