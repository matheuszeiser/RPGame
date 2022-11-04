from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from armors.models import Armor
from .serializer import ArmorSerializer

class ArmorDetailView(generics.UpdateAPIView, generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = [ArmorSerializer]
    queryset = Armor.objects

from armors.serializer import ArmorSerializer


class CreateListArmorView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer
