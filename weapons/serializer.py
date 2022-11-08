from rest_framework import serializers

from weapons.models import Weapon


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ["id", "name", "damage", "category", "inventory"]

        read_only_fields = ["inventory"]

    def validate_name(self, value):
        name = Weapon.objects.filter(name=value).first()
        if name:
            raise serializers.ValidationError("This weapon has already been created")
        return value


class WeaponListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ["id", "name", "damage", "category"]
