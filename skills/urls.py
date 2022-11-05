from django.urls import path
from . import views

urlpatterns = [
    path("admin/categories/<pk>/skills/", views.CreateSkillView().as_view()),
    path("admin/skills/<pk>/",
         views.ListUpdateDeleteSkillView().as_view()),
    path("categories/<pk>/skills/",
         views.ListSkillsPerCategoryView().as_view()),
    path("categories/skills/<pk>/",
         views.ListUpdateDeleteSkillView().as_view()),
]
