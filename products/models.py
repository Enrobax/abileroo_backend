from django.db import models

from shops.models import Shop


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=50, null=False)
    product_image = models.ImageField(upload_to='images/', null=True)
    description = models.TextField()
    price = models.FloatField(null=False)
    available_amount = models.IntegerField(null=False)


