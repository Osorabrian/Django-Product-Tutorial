from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'serial_number', 'price', 'stock_size']
    list_filter = ['name', 'listed', 'price']
    search_fields = ['name', 'serial_number']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'listed'
    raw_id_fields = ['retailer']
    ordering = ['listed', 'name', 'price']
