from rest_framework.permissions import BasePermission
from rest_framework.views import Request, View

from accounts.models import Account


class IsAccountOwner(BasePermission):
    def has_object_permission(
        self,
        request: Request,
        view: View,
        obj: Account,
    ):
        return request.user == obj
