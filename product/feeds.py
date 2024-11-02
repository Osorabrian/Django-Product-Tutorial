from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Product
import markdown

class LatestListings(Feed):
    title = 'Latest Listings'
    link = reverse_lazy('product:products_list')
    description = 'This are the latest listings'
    
    def items(self):
        return Product.objects.order_by('-updated')
    
    def item_title(self, item):
        return item.name
    
    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.description), 15)
    
    def item_listdate(self, item):
        return item.listed