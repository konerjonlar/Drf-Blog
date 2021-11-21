from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsOwner(permissions.IsAuthenticatedOrReadOnly):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        # return request.user and super().has_permission() -- request.user.is_authenticated()
        return request.user and super().has_permission()

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
