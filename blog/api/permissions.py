from rest_framework import permissions


class IsCommentUserReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.comment_owner

    # def has_object_permission(self, request, view, obj):
    #     if view.action in ("update", "delete"):
    #         return request.user == obj.from_user
    #     return True
