from rest_framework.permissions import BasePermission


__author__ = 'kevinccbsg'


class UserPermission(BasePermission):

    def has_permission(self, request, view):

        from users.api import UserDetailAPI
        if request.method == "POST":
            return True
        if request.user.is_superuser:
            return True
        if isinstance(view, UserDetailAPI):
            return True
        return False

    def has_object_permission(self, request, view, obj):

        return request.user.is_superuser or request.user == obj
