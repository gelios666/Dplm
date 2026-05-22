from .models import Product


def create_product(user, validated_data):
    product = Product.objects.create(
        shop=user,
        **validated_data
    )

    return product