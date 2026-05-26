from django.db import transaction

from .models import (
    Cart,
    CartItem,
)

from catalog.models import Product

from orders.models import (
    Order,
    OrderItem,
)


def get_or_create_cart(user):
    cart, created = Cart.objects.get_or_create(
        buyer=user,
    )

    return cart


def add_product_to_cart(
    user,
    product_id,
    quantity,
):
    cart = get_or_create_cart(user)

    product = Product.objects.get(
        id=product_id,
    )

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={
            'quantity': quantity,
        }
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    return cart_item


def clear_cart(cart):
    cart.items.all().delete()


@transaction.atomic
def checkout_cart(user):
    cart = get_or_create_cart(user)

    items = cart.items.all()

    order = Order.objects.create(
        buyer=user,
    )

    total_sum = 0

    for item in items:
        item_total = (
            item.product.price * item.quantity
        )

        total_sum += item_total

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price,
        )

    order.total_sum = total_sum
    order.save()

    clear_cart(cart)

    return order