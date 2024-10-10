from django.db import models
from django.utils import timezone
from retailer.models import Retailer

# Create your models here.
class Product(models.Model):
    
    class Size(models.TextChoices):
        SMALL = 'SM', 'Small'
        MEDIUM = 'M', 'Medium'
        LARGE = 'L', 'Large'
        EXTRA_LARGE = 'XL', 'Extra large'
        
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    
    size = models.CharField(
        max_length=2,
        choices=Size.choices,
        default=Size.MEDIUM
    )
    
    price = models.IntegerField()
    serial_number = models.CharField(max_length=250)
    stock_size = models.IntegerField()
    
    retailer = models.ForeignKey(
        Retailer,
        auto_delete = models.CASCADE,
        related_name = 'products'
    )
    
    listed = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-listed']
        indexes = [
            models.Index(fields=('-listed',))
            ]
        
        
    