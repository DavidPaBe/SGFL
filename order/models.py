from django.db import models
from decimal import Decimal
from product.models import Product

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    cambio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    product = models.ManyToManyField(Product)
    quantity = models.IntegerField(default=1)

        