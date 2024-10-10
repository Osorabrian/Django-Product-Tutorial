from django.shortcuts import get_object_or_404,render
from .models import Retailer

# Create your views here.
def retailers_list(request):
    retailers = Retailer.objects.all()
    return render(request, 'retailer/list.html', {'retailers': retailers})

def reteilers_detail(request, id):
    retailer = get_object_or_404(
        Retailer,
        id=id
    )
    return render(request, 'retialer/detail.html', {'retailer': retailer})