from rest_framework import generics
from weapons.models import Weapon

from weapons.serializer import WeaponSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

class WeaponAdminView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = WeaponSerializer
    queryset = Weapon.objects


class WeaponDetailView(generics.UpdateAPIView, generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = WeaponSerializer
    queryset = Weapon.objects
    lookup_url_kwarg = "weapon_id"
