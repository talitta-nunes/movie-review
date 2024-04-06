import ipdb
from rest_framework.permissions import SAFE_METHODS, BasePermission

from users.models import User


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            if request.user.is_authenticated and request.user.is_superuser:
                return True
            return False
        return True


class CriticOnly(BasePermission):
    def has_obj_permission(self, request, view, user: User):
        if user.is_critic.id == request.user.id or request.user.is_superuser:
            return True
        return False
