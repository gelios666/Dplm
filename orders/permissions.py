from rest_framework.permissions import BasePermission


class IsBuyerOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.type == 'buyer'
        )


class IsOrderOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.buyer == request.user