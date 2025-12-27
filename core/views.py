from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Product

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html', {'message': ' helllllllllllo baby'})

def products(request):
    return render(request, 'core/products.html')

def contact(request):
    return render(request, 'core/contact.html')

def sample(request):
    if request.method == 'POST':
        return HttpResponse("POST received")
    
    return render(request, 'core/sample.html')

def base(request):
    return render(request, 'core/base.html')

def title(request):
    return render(request, 'core/title.html')

def product_detail(request, product_id):
    product = get_list_or_404(Product, id=product_id)
    return render(request, 'core/product_detail.html', {"product": product})