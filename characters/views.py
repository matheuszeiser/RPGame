from rest_framework import generics
from django.shortcuts import get_object_or_404
from .serializers import CharacterSerializer, CharacterEditSerializer
from .models import Character
from rest_framework.authentication import TokenAuthentication
from inventories.models import Inventory
from categories.models import Category
from attributes.models import Attribute
from rest_framework.views import Response
from rest_framework.views import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCharOwnerOrSuperuser


class CreateListCharacterView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CharacterSerializer
    queryset = Character.objects

    def perform_create(self, serializer):
        category_name = self.request.data["category_name"]
        if category_name == "Warrior":
            attribute = Attribute.objects.create(strength=5)
        elif category_name == "Wizard":
            attribute = Attribute.objects.create(intelligence=5)
        elif category_name == "Archer":
            attribute = Attribute.objects.create(agility=5)
        else:
            return Response(
                {"Detail": "The category name must be `Warrior`, `Wizard` or `Archer`"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        category = get_object_or_404(Category, name=category_name)
        inventory = Inventory.objects.create()

        serializer.save(
            category=category,
            attributes=attribute,
            account=self.request.user,
            inventory=inventory,
        )


class RetrieveUpdateDeleteCharView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCharOwnerOrSuperuser]

    serializer_class = CharacterEditSerializer
    queryset = Character.objects
