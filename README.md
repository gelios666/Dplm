# 🛒 Retail Shop API (Django REST Framework)

Backend-приложение для автоматизации закупок в розничной сети через REST API.

---

# 🚀 Описание проекта

Сервис позволяет:

## 👤 Пользователям:
- регистрироваться и авторизоваться
- просматривать каталог товаров
- добавлять товары в корзину
- оформлять заказы
- получать email уведомления о заказе

## 🏪 Поставщикам (расширяемо):
- управлять товарами
- загружать прайсы (YAML импорт)
- отслеживать заказы

---

# ⚙️ Технологии

- Python 3.11
- Django
- Django REST Framework
- PostgreSQL
- drf-spectacular (Swagger)
- django-filter
- SimpleJWT

---

# 📦 Основной функционал

## 👤 Users API
- регистрация
- логин (JWT)
- профиль пользователя

## 📦 Catalog API
- категории товаров
- товары
- импорт товаров из YAML

## 🛒 Cart API
- добавление товаров
- удаление товаров
- просмотр корзины

## 📑 Orders API
- создание заказа из корзины
- просмотр списка заказов
- просмотр деталей заказа

---

# 📧 Email уведомления

При оформлении заказа система отправляет:

## 1. Администратору:
- состав заказа
- количество товаров
- итоговая сумма

## 2. Клиенту:
- подтверждение заказа
- список товаров
- сумма заказа
- статус заказа

---

# 📥 Импорт товаров (YAML)

Поддерживается загрузка товаров из YAML файлов:

```bash
python manage.py import_yaml data/shop1.yaml



## API документация

Swagger UI доступен по адресу:

/api/schema/swagger-ui/

🧪 Запуск проекта
1. Установка зависимостей
pip install -r requirements.txt
2. Миграции
python manage.py makemigrations
python manage.py migrate
3. Создание суперпользователя
python manage.py createsuperuser
4. Запуск сервера
python manage.py runserver
📌 Основные endpoints
/api/users/
/api/catalog/
/api/cart/
/api/orders/
/api/schema/