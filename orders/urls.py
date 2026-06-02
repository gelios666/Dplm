from django.urls import path

from .views import (
    OrderListCreateView,
    OrderDetailView,
    OrderStatusUpdateView,
    AddressListCreateView,
    AddressDeleteView,
    SupplierOrderListView,
)

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='orders_list_create'),

    path('<int:pk>/', OrderDetailView.as_view(), name='order_detail'),

    # изменение статуса заказа
    path(
        '<int:pk>/status/',
        OrderStatusUpdateView.as_view(),
        name='order-status-update',
    ),

    # адреса доставки
    path(
        'addresses/',
        AddressListCreateView.as_view(),
        name='addresses',
    ),

    path(
        'addresses/<int:pk>/',
        AddressDeleteView.as_view(),
        name='address_delete',
    ),

    # заказы поставщика
    path(
        'supplier/',
        SupplierOrderListView.as_view(),
        name='supplier-orders',
    ),
]