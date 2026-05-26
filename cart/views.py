from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from users.permissions import IsBuyer

from .models import Cart
from .serializers import (
    CartSerializer,
    AddToCartSerializer,
)

from .services import (
    checkout_cart,
)


class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer

    permission_classes = (
        IsAuthenticated,
        IsBuyer,
    )

    def get_object(self):
        cart, created = Cart.objects.get_or_create(
            buyer=self.request.user,
        )

        return cart


class AddToCartView(APIView):
    permission_classes = (
        IsAuthenticated,
        IsBuyer,
    )

    def post(self, request):
        serializer = AddToCartSerializer(
            data=request.data,
            context={
                'request': request,
            }
        )

        serializer.is_valid(
            raise_exception=True,
        )

        cart_item = serializer.save()

        return Response(
            {
                'message': 'Product added to cart',
                'cart_item_id': cart_item.id,
            },
            status=status.HTTP_201_CREATED,
        )


class CheckoutView(APIView):
    permission_classes = (
        IsAuthenticated,
        IsBuyer,
    )

    def post(self, request):
        order = checkout_cart(
            request.user,
        )

        return Response(
            {
                'message': 'Order created successfully',
                'order_id': order.id,
            },
            status=status.HTTP_201_CREATED,
        )