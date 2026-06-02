from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsBuyer

from .models import Cart, CartItem
from .serializers import (
    CartSerializer,
    AddToCartSerializer,
)


# =========================
# CART DETAIL
# =========================
class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated, IsBuyer)

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(
            buyer=self.request.user
        )
        return cart


# =========================
# ADD TO CART
# =========================
class AddToCartView(APIView):
    permission_classes = (IsAuthenticated, IsBuyer)

    def post(self, request):
        serializer = AddToCartSerializer(
            data=request.data,
            context={'request': request}
        )

        serializer.is_valid(raise_exception=True)
        cart_item = serializer.save()

        return Response(
            {
                'message': 'Product added to cart',
                'cart_item_id': cart_item.id,
            },
            status=status.HTTP_201_CREATED,
        )


# =========================
# REMOVE ONE ITEM
# =========================
class RemoveFromCartView(APIView):
    permission_classes = (IsAuthenticated, IsBuyer)

    def delete(self, request, item_id):
        try:
            item = CartItem.objects.get(
                id=item_id,
                cart__buyer=request.user
            )
        except CartItem.DoesNotExist:
            return Response(
                {'error': 'Item not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        item.delete()

        return Response(
            {'message': 'Item removed from cart'},
            status=status.HTTP_204_NO_CONTENT
        )


# =========================
# REDUCE QUANTITY (PATCH)
# =========================
class UpdateCartItemView(APIView):
    permission_classes = (IsAuthenticated, IsBuyer)

    def patch(self, request, item_id):
        try:
            item = CartItem.objects.get(
                id=item_id,
                cart__buyer=request.user
            )
        except CartItem.DoesNotExist:
            return Response(
                {'error': 'Item not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        quantity = request.data.get('quantity')

        if not quantity or int(quantity) <= 0:
            item.delete()
            return Response(
                {'message': 'Item removed because quantity <= 0'},
                status=status.HTTP_200_OK
            )

        item.quantity = int(quantity)
        item.save()

        return Response(
            {
                'message': 'Quantity updated',
                'item_id': item.id,
                'quantity': item.quantity,
            },
            status=status.HTTP_200_OK
        )


# =========================
# CLEAR CART
# =========================
class ClearCartView(APIView):
    permission_classes = (IsAuthenticated, IsBuyer)

    def delete(self, request):
        cart, _ = Cart.objects.get_or_create(
            buyer=request.user
        )

        cart.items.all().delete()

        return Response(
            {'message': 'Cart cleared'},
            status=status.HTTP_204_NO_CONTENT
        )


# =========================
# CHECKOUT
# =========================
class CheckoutView(APIView):
    permission_classes = (IsAuthenticated, IsBuyer)

    def post(self, request):
        from .services import checkout_cart

        order = checkout_cart(request.user)

        return Response(
            {
                'message': 'Order created successfully',
                'order_id': order.id,
            },
            status=status.HTTP_201_CREATED,
        )