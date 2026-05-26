from django.db import models

from users.models import User
from catalog.models import Product


class Cart(models.Model):
    buyer = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f'Cart {self.id} - {self.buyer.email}'


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='cart_items',
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        unique_together = (
            'cart',
            'product',
        )

    def __str__(self):
        return f'{self.product.title} x {self.quantity}'