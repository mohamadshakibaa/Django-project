from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.views.decorators.http import require_POST
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


def product_list(request):
    products = Product.objects.active()
    return render(request, 'core/product_list.html', {"products": products})


def product_detail(request, product_id):
    product = get_list_or_404(Product, id=product_id)
    return render(request, 'core/product_detail.html', {"product": product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Product Created")
    
    else:
        form = ProductForm()
    
    return render(request, 'core/product_form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("core:product_detail", pk=pk)
    else:
        form = ProductForm(instance=product)

    return render(request, "core/product_form.html", {"form": form})


def product_delete(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == "POST":
        product.delete()
        return redirect("core:product_list")

    return render(request, "core/product_confirm_delete.html", {"product": product})


# def activate_product(request, pk):
#     product = get_list_or_404(Product, id=pk)
#     product.is_available = True
#     product.save()
#     return HttpResponse("Activated")


# def cart_add(request, product_id):
#     product = get_list_or_404(Product, id=product_id)
    
#     cart = request.session.get('cart', {})
    
#     product_id_str = str(product.id)
    
#     if product_id_str in cart:
#         cart[product_id_str]['quantity'] += 1
#     else:
#         cart[product_id_str] = {'quantity': 1}
    
#     request.session['cart'] = cart
#     request.session.modified = True
    
#     return redirect('core:cart_detail')


# def cart_detail(request):
#     cart = request.session.get('cart', {})
#     product_ids = cart.keys()

#     products = Product.objects.filter(id__in=product_ids)

#     cart_items = []
#     total_price = 0

#     for product in products:
#         item = cart[str(product.id)]
#         item_total = product.get_final_price() * item['quantity']

#         cart_items.append({
#             'product': product,
#             'quantity': item['quantity'],
#             'item_total': item_total
#         })

#         total_price += item_total

#     return render(request, 'core/cart_detail.html', {
#         'cart_items': cart_items,
#         'total_price': total_price
#     })


# @require_POST
# def cart_decrease(request, product_id):
#     cart = request.session.get('cart', {})
#     pid = str(product_id)

#     if pid in cart:
#         cart[pid]['quantity'] -= 1

#         if cart[pid]['quantity'] <= 0:
#             del cart[pid]

#     request.session['cart'] = cart
#     request.session.modified = True

#     return redirect('core:cart_detail')

