from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})
