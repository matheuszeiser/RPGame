from rest_framework import serializers
from .models import Attribute


class AttributeSerializer(serializers.Serializer):
    class Meta:
        model = Attribute

        fields = ["id", "strength", "agility", "intelligence", "enurance"]
