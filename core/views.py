from django.shortcuts import render
from django.http import HttpResponse

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
