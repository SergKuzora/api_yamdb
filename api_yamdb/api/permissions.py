from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, SAFE_METHODS


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsAdminOrReadOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.role == 'admin'
                or request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        return (request.user.role == 'admin'
                or request.user.is_staff)


class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin

