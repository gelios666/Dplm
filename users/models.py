from django.contrib.auth.models import AbstractUser
from django.db import models


USER_TYPE_CHOICES = (
    ('shop', 'Магазин'),
    ('buyer', 'Покупатель'),
)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='buyer'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email