from rest_framework import serializers

from .models import Order, OrderItem
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

        read_only_fields = ('price',)


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    buyer = serializers.StringRelatedField(read_only=True)

    # 🔥 используем модельную логику (лучше чем пересчитывать тут)
    total_sum = serializers.ReadOnlyField()

    class Meta:
        model = Order

        fields = (
            'id',
            'buyer',
            'status',
            'items',
            'total_sum',
            'created_at',
        )

        read_only_fields = (
            'status',
            'created_at',
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        buyer = self.context['request'].user

        return create_order(
            buyer,
            items_data,
        )