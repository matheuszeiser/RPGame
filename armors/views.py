from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from categories.permissions import IsAdminOrReadOnly

from armors.models import Armor
from .serializer import ArmorSerializer
from armors.serializer import ArmorSerializer


class ArmorDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Armor.objects
    serializer_class = ArmorSerializer


class CreateListArmorView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer
