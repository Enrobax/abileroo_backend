from django.db import models

from products.models import Product
from shops.models import Shop


class Order(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    date_time_delivery = models.DateTimeField(null=False)
    address = models.CharField(max_length=200, null=False)
    client_email = models.EmailField(null=False)
    shipped = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="details")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    class Meta:
        db_table = 'orders_orderdetail'
        constraints = [
            models.UniqueConstraint(fields=['order', 'product'], name='unique_order_product')
        ]
