from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

# def product(request):
#     return render(request, 'myapp/products.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def product(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'myapp/products.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'myapp/product_detail.html', {'product': product})