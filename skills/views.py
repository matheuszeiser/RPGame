from rest_framework import generics
from django.shortcuts import get_object_or_404
from categories.models import Category
from skills.models import Skill

from skills.serializers import ListSkillsSerializer, SkillSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser


class CreateSkillView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = SkillSerializer
    queryset = Skill.objects

    def perform_create(self, serializer):
        category = get_object_or_404(Category, id=self.kwargs['pk'])
        skill = serializer.save()
        category.skills.add(skill)


class ListUpdateDeleteSkillView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = SkillSerializer
    queryset = Skill.objects
    pk = 'pk'


class ListSkillsPerCategoryView(generics.RetrieveAPIView):
    serializer_class = ListSkillsSerializer

    def get_queryset(self):
        return Category.objects.filter(id=self.kwargs['pk'])
