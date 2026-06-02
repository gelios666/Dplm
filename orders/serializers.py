from rest_framework import serializers

from .models import Order, OrderItem, Address
from .services import create_order


# =========================
# ADDRESS
# =========================
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'city',
            'street',
            'house',
            'apartment',
        )


# =========================
# ORDER STATUS
# =========================
class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('status',)


# =========================
# ORDER ITEM
# =========================
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


# =========================
# ORDER
# =========================
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    buyer = serializers.StringRelatedField(read_only=True)

    # адрес передаётся как ID (важно для создания заказа)
    address = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all()
    )

    total_sum = serializers.ReadOnlyField()

    class Meta:
        model = Order

        fields = (
            'id',
            'buyer',
            'address',
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
        address = validated_data.pop('address', None)
        buyer = self.context['request'].user

        return create_order(
            buyer,
            items_data,
            address=address
        )