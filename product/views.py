from django.shortcuts import get_object_or_404,render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm

class ProductListView(ListView):
    queryset = Product.objects.all() # or model = Product
    context_object_name = 'products'
    paginate_by = 3
    template_name = 'product/list.html'
    
# Create your views here.
# def products_list(request):
#     products_list = Product.objects.all()
#     paginator = Paginator(products_list, 3)
#     page_number = request.GET.get('page', 1)
#     try:
#         products = paginator.page(page_number)
#     except EmptyPage:
#         products = paginator.page(paginator.num_pages)
#     except PageNotAnInteger:
#         products = paginator.page(1)     
#     return render(request, 'product/list.html', {'products': products})

def product_details(request, year, month, day, post):
    product = get_object_or_404(
        Product,
        slug=post,
        listed__year = year,
        listed__month = month,
        listed__day = day
    )
    return render(request, 'product/detail.html', {'product': product})

def post_form(request, id):
    post = get_object_or_404(
        Product,
        id=id
    )
    
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = EmailPostForm()
    
    return render(
        request,
        'product/share.html'
    )