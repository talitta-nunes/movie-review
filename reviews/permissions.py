from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.views import Request


class PostPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated


class DeletePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return request.user.is_authenticated
