from rest_framework import serializers

from .models import (
    Category,
    Product,
)
from .services import create_product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = (
            'id',
            'name',
        )


class ProductSerializer(serializers.ModelSerializer):
    shop = serializers.StringRelatedField(
        read_only=True,
    )

    category_name = serializers.CharField(
        source='category.name',
        read_only=True,
    )

    class Meta:
        model = Product

        fields = (
            'id',
            'shop',
            'category',
            'category_name',
            'title',
            'description',
            'price',
            'quantity',
            'is_active',
            'created_at',
        )

    def create(self, validated_data):
        user = self.context['request'].user

        return create_product(
            user,
            validated_data,
        )