from django.shortcuts import get_object_or_404,render
from .models import Product

# Create your views here.
def products_list(request):
    products = Product.objects.all()
    return render(request, 'product/list.html', {'products': products})

def product_details(request, year, month, day, post):
    product = get_object_or_404(
        Product,
        slug=post,
        listed__year = year,
        listed__month = month,
        listed__day = day
    )
    return render(request, 'product/detail.html', {'product': product})