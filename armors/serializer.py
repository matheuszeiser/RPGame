from rest_framework import serializers

from armors.models import Armor


class ArmorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armor

        fields = [
            "id",
            "name",
            "defense",
            "category",
            "inventory",
        ]
        read_only_fields = ["inventory"]


class ArmorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armor
        fields = ["id", "name", "defense", "category"]
