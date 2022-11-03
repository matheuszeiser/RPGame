from rest_framework import permissions


class IsCharacterOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, character):
        return character.account == request.user
