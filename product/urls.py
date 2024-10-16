from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path('', views.products_list, name="products_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.product_details, name="product_details")
]