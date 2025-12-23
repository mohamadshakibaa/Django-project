from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('title/', views.title, name='title'),
]