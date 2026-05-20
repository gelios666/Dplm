from rest_framework.permissions import BasePermission


class IsShopOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.type == 'shop'


class IsBuyer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.type == 'buyer'