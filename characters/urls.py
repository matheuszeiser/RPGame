from django.urls import path
from . import views

urlpatterns = [
    path("char/", views.CreateListCharacterView.as_view()),
    path("char/<pk>/", views.RetrieveUpdateDeleteCharView.as_view()),
    path("char/<char_id>/weapon/<weapon_id>/",
         views.AddWeaponInInventoryView.as_view()),
    path("char/<char_id>/weapon/<armor_id>/",
         views.AddArmorInInventoryView.as_view()),
]
