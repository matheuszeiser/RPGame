from rest_framework import generics

from accounts.models import Account
from accounts.serializers import AccountSerializer


class CreateAccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
