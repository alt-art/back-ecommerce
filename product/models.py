from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    score = models.IntegerField()
    imageURL = models.CharField(max_length=2083)

    def __str__(self):
        return self.name
