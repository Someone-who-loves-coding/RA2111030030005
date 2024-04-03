from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.CharField(max_length=50)
    rating = models.FloatField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
