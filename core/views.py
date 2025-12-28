from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm


def base(request):
    return render(request, 'core/base.html')

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


def cart_add(request, product_id):
    product = get_list_or_404(Product, id=product_id)
    
    cart = request.session.get('cart', {})
    
    product_id_str = str(product.id)
    
    if product_id_str in cart:
        cart[product_id_str]['quantity'] += 1
    else:
        cart[product_id_str] = {'quantity': 1}
    
    request.session['cart'] = cart
    request.session.modified = True
    
    return redirect('core:cart_detail')


def cart_detail(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    
    products = Product.objects.filter(id__in=product_ids)
    
    cart_items = []
    
    for product in products:
        item = cart[str(product.id)]
        cart_items.append({
            'product': product,
            'quantity': item['quantity'],
            'total_price': product.get_final_price() * item['quantity']
        })
        
    return render(request, 'core/cart_detail.html', {'cart_items': cart_items})