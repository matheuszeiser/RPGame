from rest_framework import serializers

from inventories.models import Inventory
from weapons.serializer import WeaponListSerializer
from armors.serializer import ArmorListSerializer


class InventoryGeneralSerializer(serializers.ModelSerializer):

    weapons = WeaponListSerializer(read_only=True, many=True)
    armors = ArmorListSerializer(read_only=True, many=True)

    class Meta:
        model = Inventory

        fields = [
            "armors",
            "weapons",
        ]
