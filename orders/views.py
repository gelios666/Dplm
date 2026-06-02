from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Order, Address
from .serializers import (
    OrderSerializer,
    AddressSerializer,
    OrderStatusSerializer
)

from .filters import OrderFilter
from users.permissions import IsBuyer, IsShop


# =========================
# ORDERS (BUYER)
# =========================
class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, IsBuyer)

    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrderFilter

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, IsBuyer)

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)


# =========================
# ORDER STATUS (SHOP ONLY)
# =========================
class OrderStatusUpdateView(generics.UpdateAPIView):
    serializer_class = OrderStatusSerializer
    permission_classes = (IsAuthenticated, IsShop)

    queryset = Order.objects.all()


# =========================
# ADDRESS API (BUYER)
# =========================
class AddressListCreateView(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated, IsBuyer)

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddressDeleteView(generics.DestroyAPIView):
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated, IsBuyer)

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)


class SupplierOrderListView(ListAPIView):
    permission_classes = (IsAuthenticated, IsShop)
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(
            items__product__shop__owner=self.request.user
        ).distinct()