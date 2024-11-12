from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=0, null=False, blank=False, validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    def __str__(self):
        return str(self.title)
