from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.user.username}\'s cart has {self.quantity} {self.product.name}'
