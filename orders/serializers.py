from rest_framework import serializers

from .models import (
    Order,
    OrderItem,
)

from catalog.models import Product

from .services import create_order


class OrderItemSerializer(serializers.ModelSerializer):
    product_title = serializers.CharField(
        source='product.title',
        read_only=True,
    )

    class Meta:
        model = OrderItem

        fields = (
            'id',
            'product',
            'product_title',
            'quantity',
            'price',
        )

        read_only_fields = (
            'price',
        )


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(
        many=True,
    )

    buyer = serializers.StringRelatedField(
        read_only=True,
    )

    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order

        fields = (
            'id',
            'buyer',
            'status',
            'items',
            'total_price',
            'created_at',
        )

        read_only_fields = (
            'status',
            'created_at',
        )

    def get_total_price(self, obj):
        total = 0

        for item in obj.items.all():
            total += item.price * item.quantity

        return total

    def create(self, validated_data):
        items_data = validated_data.pop('items')

        buyer = self.context['request'].user

        return create_order(
            buyer,
            items_data,
        )