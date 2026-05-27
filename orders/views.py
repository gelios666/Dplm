from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from .models import Order
from .serializers import OrderSerializer
from .filters import OrderFilter

from users.permissions import IsBuyer


class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    permission_classes = (
        IsAuthenticated,
        IsBuyer,
    )

    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrderFilter

    def get_queryset(self):
        return Order.objects.filter(
            buyer=self.request.user
        )


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer

    permission_classes = (
        IsAuthenticated,
        IsBuyer,
    )

    def get_queryset(self):
        return Order.objects.filter(
            buyer=self.request.user
        )