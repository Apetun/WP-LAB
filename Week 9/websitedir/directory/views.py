from django.shortcuts import render, redirect
from .forms import CategoryForm, PageForm
from .models import Category, Page

def index(request):
    return render(request, 'directory/index.html')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_categories')
    else:
        form = CategoryForm()
    return render(request, 'directory/add_category.html', {'form': form})

def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_pages')
    else:
        form = PageForm()
    return render(request, 'directory/add_page.html', {'form': form})

def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'directory/list_categories.html', {'categories': categories})

def list_pages(request):
    pages = Page.objects.all()
    return render(request, 'directory/list_pages.html', {'pages': pages})

