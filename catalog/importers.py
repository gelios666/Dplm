import yaml

from .models import (
    Shop,
    Category,
    Product,
    ProductInfo,
)


def import_shop_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    # shop
    shop, _ = Shop.objects.update_or_create(
        name=data['shop'],
    )

    # categories
    for category_data in data['categories']:
        Category.objects.update_or_create(
            id=category_data['id'],
            defaults={
                'name': category_data['name'],
                'shop': shop,
            }
        )

    # products
    for item in data['goods']:

        product, _ = Product.objects.update_or_create(
            external_id=item['id'],
            defaults={
                'shop': shop,
                'category_id': item['category'],
                'title': item['name'],
                'description': item.get('model', ''),
                'price': item['price'],
                'quantity': item['quantity'],
            }
        )

        # parameters
        parameters = item.get('parameters', {})

        for name, value in parameters.items():
            ProductInfo.objects.update_or_create(
                product=product,
                name=name,
                defaults={
                    'value': value,
                }
            )
