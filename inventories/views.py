from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .permissions import IsCharacterOwner

from inventories.models import Inventory
from inventories.serializers import InventoryGeneralSerializer
from characters.models import Character


class RetrieveInventoryView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsCharacterOwner]

    queryset = Inventory.objects
    serializer_class = InventoryGeneralSerializer

    def get_object(self):
        character = get_object_or_404(Character, id=self.kwargs["pk"])
        self.check_object_permissions(self.request, character)
        inventory = get_object_or_404(Inventory, character=character)
        return inventory
