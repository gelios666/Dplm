from rest_framework import serializers

from .models import (
    Cart,
    CartItem,
)

from catalog.models import Product

from .services import (
    add_product_to_cart,
)


class CartItemSerializer(serializers.ModelSerializer):
    product_title = serializers.CharField(
        source='product.title',
        read_only=True,
    )

    product_price = serializers.DecimalField(
        source='product.price',
        max_digits=10,
        decimal_places=2,
        read_only=True,
    )

    class Meta:
        model = CartItem

        fields = (
            'id',
            'product',
            'product_title',
            'product_price',
            'quantity',
        )


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Cart

        fields = (
            'id',
            'buyer',
            'items',
            'created_at',
            'updated_at',
        )


class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def save(self, **kwargs):
        user = self.context['request'].user

        return add_product_to_cart(
            user=user,
            product_id=self.validated_data['product_id'],
            quantity=self.validated_data['quantity'],
        )