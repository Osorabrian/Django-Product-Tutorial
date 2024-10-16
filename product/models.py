from django.db import models
from django.utils import timezone
from django.urls import reverse

class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(stock_size__gt = 0)
    
# product model
class Product(models.Model):
    
    class Size(models.TextChoices):
        SMALL = 'SM', 'Small'
        MEDIUM = 'M', 'Medium'
        LARGE = 'L', 'Large'
        EXTRA_LARGE = 'XL', 'Extra large'
        
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='listed')
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
        'retailer.Retailer',
        on_delete=models.CASCADE,
        related_name='products',
        default=''
    )
    
    listed = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = models.Manager()
    stocked = ProductManager()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse(
            'product:product_details',
            args=[
            self.listed.year,
            self.listed.month,
            self.listed.day,
            self.slug
            ]
        )
    
    class Meta:
        ordering = ['-listed']
        indexes = [
            models.Index(fields=('-listed',))
            ]
        
        
    