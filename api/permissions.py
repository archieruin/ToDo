from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerList(BasePermission):
    def has_object_permission(self, request, view, obj):
        # if request.method in SAFE_METHODS:
        #     return True
        return obj.user == request.user


class IsOwnerTask(BasePermission):
    def has_object_permission(self, request, view, obj):
        # if request.method in SAFE_METHODS:
        #     return True
        return obj.list.user == request.user
