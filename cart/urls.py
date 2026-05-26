from django.urls import path

from .views import (
    CartDetailView,
    AddToCartView,
    CheckoutView,
)


urlpatterns = [
    path(
        '',
        CartDetailView.as_view(),
        name='cart-detail',
    ),

    path(
        'add/',
        AddToCartView.as_view(),
        name='add-to-cart',
    ),

    path(
        'checkout/',
        CheckoutView.as_view(),
        name='checkout',
    ),
]