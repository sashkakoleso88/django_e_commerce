from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=228)
    price = models.IntegerField()
    description = models.CharField(max_length=228)
