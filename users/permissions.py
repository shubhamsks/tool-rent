from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSelfOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.username == view.kwargs['username']


class IsSelf(BasePermission):
    def has_permission(self, request, view):
        return request.user.username == view.kwargs['username']
