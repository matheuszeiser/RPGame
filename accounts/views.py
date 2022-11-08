from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from accounts.models import Account
from accounts.permissions import IsAccountOwner
from accounts import serializers


class CreateAccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = serializers.AccountSerializer


class RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Account.objects.all()
    serializer_class = serializers.AccountSerializer

    def perform_destroy(self, instance: Account):
        setattr(instance, "is_active", False)

        instance.save()


class AdminListAccountsView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Account.objects.all()
    serializer_class = serializers.AccountSerializer


class AdminActivateDeleteAccountView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Account.objects.all()
    serializer_class = serializers.ActivateDeactivateAccountSerializer
