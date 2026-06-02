from django.db import models

from users.models import User


class Shop(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shops',
        null=True,
        blank=True,
    )

    name = models.CharField(max_length=255)

    url = models.URLField(
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='categories',
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='products',
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
    )

    external_id = models.PositiveIntegerField(
        unique=True,
    )

    title = models.CharField(max_length=255)

    description = models.TextField(
        blank=True,
        null=True,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    quantity = models.PositiveIntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title


class ProductInfo(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='parameters',
    )

    name = models.CharField(max_length=255)

    value = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}: {self.value}'