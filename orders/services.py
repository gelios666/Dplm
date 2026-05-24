from .models import (
    Order,
    OrderItem,
)

from catalog.models import Product


def create_order(buyer, items_data):
    order = Order.objects.create(
        buyer=buyer,
    )

    for item_data in items_data:
        product = item_data['product']

        quantity = item_data['quantity']

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price,
        )

    return order