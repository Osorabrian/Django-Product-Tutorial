from django.db import models
from django.utils import timezone

# Create your models here.
class Retailer(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    registered = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [models.Index(fields=('name',))]