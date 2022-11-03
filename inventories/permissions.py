from rest_framework.permissions import BasePermission
from rest_framework.views import Request, View

from characters.models import Character


class IsCharacterOwner(BasePermission):
    def has_object_permission(
        self,
        request: Request,
        view: View,
        character: Character,
    ):
        return request.user == character.account
