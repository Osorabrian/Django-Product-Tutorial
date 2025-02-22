from django.shortcuts import get_object_or_404,render
from .models import Product, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from .forms import EmailProductForm, CommentForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count
 
# class ProductListView(ListView):
#     queryset = Product.objects.all() # or model = Product
#     context_object_name = 'products'
#     paginate_by = 3
#     template_name = 'product/list.html'
    
# Create your views here.
def products_list(request, tag_slug = None):
    products_list = Product.objects.all()
    
    tags = None
    if tag_slug:
        tags = get_object_or_404(Tag, slug = tag_slug)
        products_list = products_list.filter(tags__in=[tags])
        
    paginator = Paginator(products_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        products = paginator.page(page_number)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        products = paginator.page(1)     
    return render(request, 'product/list.html', {'products': products, "tags": tags})

def product_details(request, year, month, day, post):
    product = get_object_or_404(
        Product,
        slug=post,
        listed__year = year,
        listed__month = month,
        listed__day = day
    )
    
    products_tags = product.tags.values_list('id', flat=True)
    similar_products = Product.objects.filter(tags__in=products_tags).exclude(id=product.id).annotate(same_tags = Count("tags")).order_by("-same_tags", "-listed")
    
    comments = product.comments.filter(active=True)
    form = CommentForm()
    return render(request, 'product/detail.html', {'product': product, 'comments': comments, 'form': form, "similar_products": similar_products})

def product_share(request, id):
    product = get_object_or_404(
        Product,
        id=id
    )
    sent = False
    
    if request.method == 'POST':
        form = EmailProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            product_url = request.build_absolute_uri(
                product.get_absolute_url
            )
            subject = (
                f"{cd['name']} ({cd['email']})"
                f"recommends you to check out {product.name}"
            )
            
            message = (
                f"Check out {product.name} at {product_url}"
            )
            
            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=[cd['to']]
            )
            
            sent=True
    else:
        form = EmailProductForm()
    
    return render(
        request,
        'product/share.html',
        {'form': form, 'product': product, 'sent': sent}
    )
    
@require_POST
def product_comment(request, id):
    product = get_object_or_404(
        Product,
        id=id
    )
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit = False)
        comment.product = product
        comment.save()
    
    return render(
        request,
        'product/comment.html',
        {'product': product, 'form': form, 'comment': comment}
    )