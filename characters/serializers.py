from rest_framework import serializers
from .models import Character
from inventories.models import Inventory
from categories.models import Category
from attributes.models import Attribute
from rest_framework.views import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import status


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"
        read_only_fields = ["created_at"]

    def perform_create(self, serializer):
        category_name = self.request["category"]
        if category_name == "Warrior":
            attribute = Attribute.objects.create(strenght=5)
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
            attribute=attribute,
            account=self.request.user,
            inventory=inventory,
        )
