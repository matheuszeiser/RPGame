from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from categories.permissions import IsAdminOrReadOnly

from armors.models import Armor
from .serializer import ArmorSerializer
from armors.serializer import ArmorSerializer


class ArmorDetailView(generics.UpdateAPIView, generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = [ArmorSerializer]
    queryset = Armor.objects


class CreateListArmorView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer
