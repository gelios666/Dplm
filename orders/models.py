from django.db import models
from users.models import User
from catalog.models import Product


ORDER_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('delivered', 'Delivered'),
)


class Address(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses'
    )

    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=50)
    apartment = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.city}, {self.street}'


class Order(models.Model):
    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
    )


    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )

    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default='pending',
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id}'

    @property
    def total_sum(self):
        return sum(
            item.quantity * item.price
            for item in self.items.all()
        )


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order_items',
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return f'{self.product.title} x {self.quantity}'