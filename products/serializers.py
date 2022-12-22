from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'shop', 'name', 'product_image', 'description', 'price', 'available_amount']


