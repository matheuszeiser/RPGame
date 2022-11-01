from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from accounts.models import Account
from accounts.permissions import IsAccountOwner
from accounts.serializers import AccountSerializer


class CreateAccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def perform_destroy(self, instance: Account):
        setattr(instance, "is_active", False)

        instance.save()
