from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from .models import Book

def create_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book = book_form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        book_form = BookForm()
    return render(request, 'library/create_book.html', {'book_form': book_form})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})
