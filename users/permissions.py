from rest_framework import permissions


class IsModer(permissions.BasePermission):
    message = 'Вы не являетесь менеджером'

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moders').exists():
            return True
        else:
            return False


class IsOwner(permissions.BasePermission):
    message = 'Вы не являетесь создателем'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        else:
            return False
