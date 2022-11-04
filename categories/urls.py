from django.urls import path
from . import views

urlpatterns = [
    path("admin/categories/", views.CreateCategoryView.as_view()),
    path("admin/categories/<pk>/", views.UpdateDeleteCategoryView.as_view()),
    path("categories/", views.ListCategoriesView.as_view())
]
