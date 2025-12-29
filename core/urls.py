from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/decrease/<int:product_id>/', views.cart_decrease, name='cart_decrease'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
