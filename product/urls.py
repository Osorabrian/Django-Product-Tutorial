from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path('', views.ProductListView.as_view(), name="products_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.product_details, name="product_details"),
    path('<int:id>/share', views.product_share, name="product_share")
]