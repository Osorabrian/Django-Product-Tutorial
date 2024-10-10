from django.contrib import admin
from .models import Retailer

# Register your models here.
@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ['name','registered','description']
    list_filter = ['name', 'registered']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'registered'
    ordering = ['name']
    show_facets = admin.ShowFacets.ALWAYS