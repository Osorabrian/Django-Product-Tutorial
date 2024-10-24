from django.shortcuts import get_object_or_404,render
from .models import Retailer
from django.views.generic import ListView
from .forms import ShareRetailer
from django.core.mail import send_mail

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

def retailer_share(request, id):
    retailer = get_object_or_404(
        Retailer,
        id=id
    )
    sent = False
    if request.method == 'POST':
        
        form = ShareRetailer(request.POST)
        if form.is_valid():
            
            cd = form.cleaned_data
            
            retailer_url = request.build_absolute_uri(
                retailer.get_absolute_url
            )
            
            subject=(f" Checkout {retailer.name} ")
            message= (f" Please checkout {retailer.name} at {retailer_url} ")
            
            send_mail(
                subject= subject,
                message=message,
                from_email = None,
                recipient_list=[cd['to']]
                
            )
            
            sent=True
    else:
        form = ShareRetailer()
                
    return render (
        request,
        'retailer/share.html',
        {'form': form, 'retailer': retailer, 'sent': sent}
    )