from django.urls import path
from .api_views import ProductListAPI

urlpatterns = [
    path("products/", ProductListAPI.as_view(), name="api_product_list"),
]
