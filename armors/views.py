from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from armors.models import Armor
from armors.serializer import ArmorSerializer


class CreateListArmorView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer
