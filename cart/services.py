from django.core.mail import send_mail
from django.conf import settings

from orders.models import Order, OrderItem

from .models import Cart, CartItem
from catalog.models import Product


def checkout_cart(user):
    cart = user.cart
    items = cart.items.select_related('product')

    if not items.exists():
        return None

    # создаём заказ
    order = Order.objects.create(buyer=user)

    order_items_text = []

    total_sum = 0

    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price,
        )

        line_total = item.quantity * item.product.price
        total_sum += line_total

        order_items_text.append(
            f"{item.product.title} x{item.quantity} = {line_total}"
        )

    # очищаем корзину
    cart.items.all().delete()

    # =========================
    # 📧 EMAIL КЛИЕНТУ
    # =========================
    send_mail(
        subject=f"Заказ #{order.id} принят",
        message="\n".join([
            "Спасибо за заказ!",
            "",
            f"Заказ #{order.id}",
            "",
            *order_items_text,
            "",
            f"ИТОГО: {total_sum}",
        ]),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )

    # =========================
    # 📧 EMAIL АДМИНУ / ПОСТАВЩИКУ
    # =========================
    send_mail(
        subject=f"Новая накладная заказ #{order.id}",
        message="\n".join([
            "НОВЫЙ ЗАКАЗ",
            "",
            f"Покупатель: {user.email}",
            "",
            *order_items_text,
            "",
            f"ИТОГО: {total_sum}",
        ]),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.ADMIN_EMAIL],
    )

    return order


def add_product_to_cart(user, product_id, quantity):
    cart, _ = Cart.objects.get_or_create(
        buyer=user,
    )

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