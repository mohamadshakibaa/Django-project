from django.db import models
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class ProductQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)
    
    def expensive(self, min_price):
        return self.filter(price__gt=min_price)
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    is_active = models.BooleanField(default=True)
    
    objects = ProductQuerySet.as_manager()
    
    def __str__(self):
        return self.name
    
    def is_available(self):
        return self.is_active
    
    def get_final_price(self):
        tax_rate = Decimal('0.09')
        return self.price + (self.price * tax_rate)
    
    
