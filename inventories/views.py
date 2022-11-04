from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from utils.utils import get_object_or_404_with_message
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
        character = get_object_or_404_with_message(Character, id=self.kwargs["pk"], msg="Character not found")
        self.check_object_permissions(self.request, character)
        inventory = get_object_or_404_with_message(Inventory, character=character, msg="Inventory not found")
        return inventory
