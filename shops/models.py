from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return f"{self.name}"

