from django.urls import path

from .views import (
    CartDetailView,
    AddToCartView,
    CheckoutView,
    RemoveFromCartView,
    UpdateCartItemView,
    ClearCartView,
)

urlpatterns = [
    path('', CartDetailView.as_view(), name='cart-detail'),

    path('add/', AddToCartView.as_view(), name='add-to-cart'),

    path('checkout/', CheckoutView.as_view(), name='checkout'),

    path('remove/<int:item_id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),

    path('update/<int:item_id>/', UpdateCartItemView.as_view(), name='update-cart-item'),

    path('clear/', ClearCartView.as_view(), name='clear-cart'),
]