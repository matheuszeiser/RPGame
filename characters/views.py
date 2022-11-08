from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, status

from armors.models import Armor
from attributes.models import Attribute
from categories.models import Category
from inventories.models import Inventory
from utils.utils import get_object_or_404_with_message
from weapons.models import Weapon

from .models import Character
from .permissions import IsCharOwner, IsCharOwnerOrSuperuser
from .serializers import CharacterEditSerializer, CharacterSerializer


class CreateListCharacterView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CharacterSerializer

    def get_queryset(self):
        return Character.objects.filter(account=self.request.user)

    def perform_create(self, serializer):
        category_name = self.request.data["category_name"]
        if category_name == "Warrior":
            attribute = Attribute.objects.create(strength=5)
        elif category_name == "Wizard":
            attribute = Attribute.objects.create(intelligence=5)
        elif category_name == "Archer":
            attribute = Attribute.objects.create(agility=5)
        else:
            return Response(
                {"Detail": "The category name must be `Warrior`, `Wizard` or `Archer`"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        category = get_object_or_404_with_message(
            Category, name=category_name, msg="Category not found"
        )
        inventory = Inventory.objects.create()

        serializer.save(
            category=category,
            attributes=attribute,
            account=self.request.user,
            inventory=inventory,
        )


class RetrieveUpdateDeleteCharView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCharOwnerOrSuperuser]

    serializer_class = CharacterEditSerializer
    queryset = Character.objects


class AddWeaponInInventoryView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCharOwner]

    def patch(self, request, char_id, weapon_id):
        character = get_object_or_404_with_message(
            Character, id=char_id, msg="Character not found"
        )
        weapon = get_object_or_404_with_message(
            Weapon, id=weapon_id, msg="Weapon not found"
        )
        self.check_object_permissions(request, character)
        if character.category.name != weapon.category:
            return Response(
                {"detail": "weapon must be the same category as the character"},
                status.HTTP_401_UNAUTHORIZED,
            )

        character.inventory.weapons.add(weapon)

        return Response({"sucess": "Weapon added"}, status.HTTP_200_OK)


class AddArmorInInventoryView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCharOwner]

    def patch(self, request, char_id, armor_id):
        character = get_object_or_404_with_message(
            Character, id=char_id, msg="Character not found"
        )
        armor = get_object_or_404_with_message(
            Armor, id=armor_id, msg="Armor not found"
        )
        self.check_object_permissions(request, character)
        if character.category.name != armor.category:
            return Response(
                {"detail": "armor must be the same category as the character"},
                status.HTTP_401_UNAUTHORIZED,
            )

        character.inventory.armors.add(armor)

        return Response({"sucess": "Armor added"}, status.HTTP_200_OK)
