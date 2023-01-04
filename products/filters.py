from django_filters import rest_framework as filters

from products.models import Product


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['shop', 'name']
