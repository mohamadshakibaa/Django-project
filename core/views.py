from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html', {'message': ' helllllllllllo baby'})


def contact(request):
    return render(request, 'core/contact.html')


def product_detail(request, product_id):
    product = get_list_or_404(Product, id=product_id)
    return render(request, 'core/product_detail.html', {"product": product})


def product_list(request):
    products = Product.objects.active()
    return render(request, 'core/list.html', {"products": products})


def activate_product(request, pk):
    product = get_list_or_404(Product, id=pk)
    product.is_available = True
    product.save()
    return HttpResponse("Activated")


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Product Created")
    
    else:
        form = ProductForm()
    
    return render(request, 'core/product_form.html', {'form': form})