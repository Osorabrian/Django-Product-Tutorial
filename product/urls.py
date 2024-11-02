from django.urls import path
from . import views
from .feeds import LatestListings

app_name = "product"

urlpatterns = [
    path('', views.products_list, name="products_list"),
    path("tag/<slug:tag_slug>", views.products_list, name="products_tag"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.product_details, name="product_details"),
    path('<int:id>/share/', views.product_share, name="product_share"),
    path('<int:id>/comment/', views.product_comment, name='product_comment'),
    path('feed/', LatestListings(), name='product_listing')
]