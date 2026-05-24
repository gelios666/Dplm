import django_filters

from .models import Order


class OrderFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(field_name='status')
    buyer = django_filters.NumberFilter(field_name='buyer__id')

    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Order
        fields = [
            'status',
            'buyer',
            'created_at',
        ]