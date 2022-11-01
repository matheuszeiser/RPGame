from rest_framework import generics
from django.shortcuts import get_object_or_404
from .serializers import CharacterSerializer
from .models import Character
from inventories.models import Inventory
from categories.models import Category
from attributes.models import Attribute
from rest_framework.views import Response


class CreateListCharacterView(generics.ListCreateAPIView):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()
