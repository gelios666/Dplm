🛒 Retail Shop API (Django + DRF)

Backend-система автоматизации интернет-магазина с корзиной, заказами, адресами доставки, поставщиками и email-уведомлениями.

🚀 Стек технологий
Python 3.11
Django 4.2
Django REST Framework
PostgreSQL
JWT (SimpleJWT)
django-filter
drf-spectacular
SMTP email
YAML импорт данных

🏗 Архитектура проекта

Система разделена на модули:

users — пользователи и роли
catalog — магазины, товары, категории
cart — корзина
orders — заказы
services — бизнес-логика (создание заказа, email)

👥 Роли пользователей
🧑 Buyer (покупатель)
управление корзиной
оформление заказов
добавление адресов доставки
просмотр своих заказов
🏪 Shop (поставщик)
управление товарами
просмотр заказов со своими товарами
изменение статуса заказа

🛒 Cart API
📌 Возможности:
добавить товар в корзину
удалить товар
изменить количество
просмотр корзины
оформление заказа (checkout)
📡 Endpoints:
GET    /api/cart/
POST   /api/cart/add/
POST   /api/cart/checkout/

📦 Orders API
📌 Возможности:
создание заказа из корзины
просмотр заказов пользователя
детальный просмотр заказа
📡 Endpoints:
GET  /api/orders/
GET  /api/orders/<id>/
POST /api/orders/

🏪 Supplier API (Shop)
📌 Возможности:
просмотр заказов с товарами магазина
фильтрация заказов по shop
📡 Endpoints:
GET /api/orders/supplier/

✏️ Order Status API
📌 Возможности:
изменение статуса заказа (shop)
📡 Endpoint:
PATCH /api/orders/status/<id>/

🏠 Address API
📌 Возможности:
добавление адреса
просмотр адресов пользователя
удаление адреса
📡 Endpoints:
GET    /api/orders/addresses/
POST   /api/orders/addresses/
DELETE /api/orders/addresses/<id>/

📥 Импорт данных (YAML)

Система поддерживает загрузку каталога:

магазины (Shop)
категории
товары
параметры товаров
📧 Email уведомления

При создании заказа:

✔ клиент получает подтверждение
✔ администратор получает накладную

🔐 Аутентификация

Используется JWT:

/api/token/
/api/token/refresh/

⚙️ Установка проекта
git clone <repo>
cd Diplom

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

📦 Миграции
python manage.py makemigrations
python manage.py migrate
👤 Создание администратора
python manage.py createsuperuser

