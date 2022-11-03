from rest_framework import serializers

from inventories.models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory

        fields = [
            "id",
            "character",
            "armors",
            "weapons"
        ]

        read_only_fields = [
            "weapons",
            "armors",
        ]
        depth = 1

