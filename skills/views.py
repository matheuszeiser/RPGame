from rest_framework import generics
from utils.utils import get_object_or_404_with_message
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
        category = get_object_or_404_with_message(
            Category, id=self.kwargs["pk"], msg="Category not found"
        )
        skill = serializer.save()
        category.skills.add(skill)


class ListUpdateDeleteSkillView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = SkillSerializer
    queryset = Skill.objects
    pk = "pk"


class ListSkillsPerCategoryView(generics.RetrieveAPIView):
    serializer_class = ListSkillsSerializer

    def get_queryset(self):
        return Category.objects.filter(id=self.kwargs["pk"])
