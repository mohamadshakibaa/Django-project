from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # path('cart/', views.cart_detail, name='cart_detail'),
    # path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    # path('cart/decrease/<int:product_id>/', views.cart_decrease, name='cart_decrease'),
    path("", views.product_list, name="product_list"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("product/add/", views.product_create, name="product_create"),
    path("product/<int:pk>/edit/", views.product_update, name="product_update"),
    path("product/<int:pk>/delete/", views.product_delete, name="product_delete"),
]
