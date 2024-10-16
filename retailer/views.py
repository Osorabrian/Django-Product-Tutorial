from django.shortcuts import get_object_or_404,render
from .models import Retailer

# Create your views here.
def retailers_list(request):
    retailers = Retailer.objects.all()
    return render(request, 'retailer/list.html', {'retailers': retailers})

def retailer_details(request, year, month, day, name):
    retailer = get_object_or_404(
        Retailer,
        registered__year = year,
        registered__month = month,
        registered__day = day,
        slug=name
    )
    return render(request, 'retailer/detail.html', {'retailer': retailer})