from django.contrib import admin

from .models import Shop, Category, Product, ProductInfo


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'owner',
        'is_active',
    )

    list_display_links = (
        'name',
    )

    search_fields = (
        'name',
    )

    list_filter = (
        'is_active',
    )

    fields = (
        'name',
        'owner',
        'url',
        'is_active',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'shop',
    )

    search_fields = (
        'name',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'shop',
        'category',
        'price',
        'quantity',
        'is_active',
    )

    list_filter = (
        'shop',
        'category',
        'is_active',
    )

    search_fields = (
        'title',
    )


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'name',
        'value',
    )

    search_fields = (
        'product__title',
        'name',
    )