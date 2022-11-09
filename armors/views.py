from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from armors.models import Armor
from .serializer import ArmorSerializer, ArmorListSerializer
from armors.serializer import ArmorSerializer


class ArmorDetailView(generics.UpdateAPIView, generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Armor.objects
    serializer_class = ArmorSerializer
    lookup_url_kwarg = "armor_id"


class ListArmorView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]

    queryset = Armor.objects
    serializer_class = ArmorListSerializer
    lookup_url_kwarg = "armor_id"


class CreateArmorView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer


class ListArmorsView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]

    queryset = Armor.objects.all()
    serializer_class = ArmorListSerializer
