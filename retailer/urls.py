from django.urls import path
from . import views

app_name = 'retailer'

urlpattern = [
    path('', views.retailers_list, name="retailers_list"),
    path('<int:id>/', views.retialer_details, name="retailer_details")
]