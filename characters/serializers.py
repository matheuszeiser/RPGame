from rest_framework import serializers
from .models import Character
from categories.serializers import CreateCategorySerializer
from attributes.serializers import AttributeSerializer
from accounts.serializers import AccountListSerializer
from inventories.serializers import InventoryGeneralSerializer


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"

        read_only_fields = ["created_at", "account", "inventory", "attributes"]
        extra_kwargs = {"category_name": {"write_only": True}}

    category = CreateCategorySerializer(read_only=True)
    account = AccountListSerializer(read_only=True)
    attributes = AttributeSerializer(read_only=True)


class CharacterEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"
        read_only_fields = ["category_name"]

    category = CreateCategorySerializer(read_only=True)
    account = AccountListSerializer(read_only=True)
    attributes = AttributeSerializer(read_only=True)
    inventory = InventoryGeneralSerializer(read_only=True)
