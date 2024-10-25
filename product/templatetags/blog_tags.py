from django import template
from ..models import Product
from django.db.models import Count

register = template.Library()

@register.simple_tag
def total_products():
    return Product.objects.all()

@register.inclusion_tag('product/latest_listings.html')
def most_recent_listings(count = 5):
    recent_listings = Product.objects.order_by('listed')[:count]
    return {'recent_listings': recent_listings}

@register.simple_tag
def most_commented_listings():
    return Product.objects.annotate( total_comments = Count('comments')).order_by('total_comments')[:3]