from django.core.mail import send_mail
from django.conf import settings
from django.db import transaction

from .models import Order, OrderItem


# =========================
# 📧 ADMIN EMAIL
# =========================
def send_order_to_admin(order: Order):
    items = order.items.select_related('product')

    items_text = "\n".join([
        f"{item.product.title} x {item.quantity} = {item.quantity * item.price}"
        for item in items
    ])

    message = f"""
📦 НОВЫЙ ЗАКАЗ #{order.id}

👤 Покупатель: {order.buyer.email}

🛒 Товары:
{items_text}

💰 ИТОГО: {order.total_sum}
"""

    send_mail(
        subject=f"Новый заказ #{order.id}",
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.ADMIN_EMAIL],
    )


# =========================
# 📧 USER EMAIL
# =========================
def send_order_to_user(order: Order):
    items = order.items.select_related('product')

    items_text = "\n".join([
        f"{item.product.title} x {item.quantity}"
        for item in items
    ])

    message = f"""
Здравствуйте!

Ваш заказ #{order.id} принят.

📦 Статус: {order.status}

🛒 Товары:
{items_text}

💰 Сумма: {order.total_sum}

Спасибо за покупку!
"""

    send_mail(
        subject=f"Заказ #{order.id} принят",
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[order.buyer.email],
    )


# =========================
# 📦 CREATE ORDER (FIXED)
# =========================
@transaction.atomic
def create_order(buyer, items_data, address=None):
    order = Order.objects.create(
        buyer=buyer,
        address=address
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

    # EMAILS (после успешного создания)
    send_order_to_admin(order)
    send_order_to_user(order)

    return order