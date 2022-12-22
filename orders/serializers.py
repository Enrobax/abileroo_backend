from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from orders.models import OrderDetail, Order


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['id', 'order', 'product', 'amount']
        validators = [
            UniqueTogetherValidator(
                queryset=OrderDetail.objects.all(),
                fields=('order', 'product')
            )
        ]

    def validate(self, data):
        product = data["product"]
        p_av_amount = product.available_amount
        if data["amount"] > p_av_amount:
            raise serializers.ValidationError("The ordered amount is larger than the available amount")
        return data


class OrderSerializer(serializers.ModelSerializer):
    details = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'shop', 'date_time_delivery', 'address', 'client_email', 'shipped', 'delivered', 'details']
