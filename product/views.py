from django.shortcuts import get_object_or_404,render
from .models import Product

# Create your views here.
def products_list(request):
    products = Product.objects.all()
    return render(request, 'product/list.html', {'products': products})

def product_details(request, id):
    product = get_object_or_404(
        Product,
        id=id
    )
    return render(request, 'product/detail.html', {'product': product})