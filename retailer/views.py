from django.shortcuts import get_object_or_404,render
from .models import Retailer
from django.views.generic import ListView

class RetailerListView(ListView):
    queryset = Retailer.objects.all()
    context_object_name='retailers'
    paginate_by=3
    template_name='retailer/list.html'
# Create your views here.
# def retailers_list(request):
#     retailers = Retailer.objects.all()
#     return render(request, 'retailer/list.html', {'retailers': retailers})

def retailer_details(request, year, month, day, name):
    retailer = get_object_or_404(
        Retailer,
        registered__year = year,
        registered__month = month,
        registered__day = day,
        slug=name
    )
    
    return render(request, 'retailer/detail.html', {'retailer': retailer})