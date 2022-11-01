from rest_framework import serializers

from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "is_superuser",
            "is_active",
            "date_joined",
        ]

        read_only_fields = [
            "is_superuser",
            "is_active",
            "date_joined",
        ]

        extra_kwargs = {"password": {"write_only": True}}
