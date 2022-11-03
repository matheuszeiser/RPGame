from rest_framework import serializers
from .models import Character
from django.shortcuts import get_object_or_404
from categories.serializers import CreateCategorySerializer
from attributes.serializers import AttributeSerializer
from accounts.serializers import AccountSerializer


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"

        read_only_fields = ["created_at", "account", "inventory", "attributes"]
        extra_kwargs = {"category_name": {"write_only": True}}

    category = CreateCategorySerializer(read_only=True)
    account = AccountSerializer(read_only=True)
    attributes = AttributeSerializer(read_only=True)
