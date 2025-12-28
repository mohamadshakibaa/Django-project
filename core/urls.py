from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path("", views.base, name="base"),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('cart_add/', views.cart_add, name="cart_add")
]