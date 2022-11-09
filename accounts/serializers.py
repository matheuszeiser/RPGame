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

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)

    def update(self, instance: Account, validated_data: dict):

        for key, value in validated_data.items():

            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance


class ActivateDeactivateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_superuser",
            "is_active",
            "date_joined",
        ]

        read_only_fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_superuser",
            "date_joined",
        ]


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "username"]
