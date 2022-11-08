from rest_framework import generics
from weapons.models import Weapon

from weapons.serializer import WeaponSerializer, WeaponListSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser


class WeaponAdminView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = WeaponSerializer
    queryset = Weapon.objects


class WeaponsListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]

    serializer_class = WeaponListSerializer
    queryset = Weapon.objects


class WeaponDetailView(generics.UpdateAPIView, generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = WeaponSerializer
    queryset = Weapon.objects
    lookup_url_kwarg = "weapon_id"


class WeaponListView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]

    serializer_class = WeaponListSerializer
    queryset = Weapon.objects
    lookup_url_kwarg = "weapon_id"
