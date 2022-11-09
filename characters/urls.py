from django.urls import path

from . import views

urlpatterns = [
    path("char/", views.CreateListCharacterView.as_view()),
    path("char/<pk>/", views.RetrieveUpdateDeleteCharView.as_view()),
    path(
        "char/<char_id>/weapon/<weapon_id>/",
        views.AddRemoveWeaponInInventoryView.as_view(),
    ),
    path(
        "char/<char_id>/armor/<armor_id>/",
        views.AddRemoveArmorInInventoryView.as_view(),
    ),
]
