from rest_framework.views import Request, View
from rest_framework import permissions
from accounts.models import Account


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        return (
            request.method == "GET"
            or request.user.is_authenticated
            and request.user.is_superuser
        )
