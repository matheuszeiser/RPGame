from rest_framework import permissions
from rest_framework.views import Request, View

# from accounts.models import Account


class IsCharOwnerOrSuperuser(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj):
        return request.user == obj.account or request.user.is_superuser


class IsCharOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj):
        return request.user == obj.account
