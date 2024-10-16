from django.urls import path
from . import views

app_name = 'retailer'

urlpatterns = [
    path('', views.retailers_list, name="retailers_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:name>', views.retailer_details, name="retailer_details")
]