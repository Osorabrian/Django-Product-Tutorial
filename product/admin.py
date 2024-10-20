from django.contrib import admin
from .models import Product, Comment

# Register Product models here.
@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'serial_number', 'price', 'stock_size']
    list_filter = ['name', 'listed', 'price']
    search_fields = ['name', 'serial_number']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'listed'
    raw_id_fields = ['retailer']
    ordering = ['listed', 'name', 'price']
    show_facets = admin.ShowFacets.ALWAYS
    
#Register comment model
@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'product', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
