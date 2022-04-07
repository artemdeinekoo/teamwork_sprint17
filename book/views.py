from django.shortcuts import render, redirect
from .models import *
from order.models import Order
from .forms import AddBookForm

def home(request):
    return render(request, 'main.html')

def book(request):
    books = Book.get_all()
    return render(request, 'book.html', {'books' : books})

def specificBook(request, id):
    specificBook = Book.get_by_id(id)
    return render(request, 'bookById.html', {'specificBook' : specificBook})

def unorderedBook(request):
    all_books = Book.objects.all()
    all_orders = Order.objects.all()
    orders_book_ids = []
    for order in all_orders:
        orders_book_ids.append(order.book.pk)

    unordered_books = []

    for book in all_books:
        if book.id not in orders_book_ids:
            unordered_books.append(book)
        else:
            continue
    return render(request, 'unorderedBooks.html', {'unordered_books' : unordered_books})

def add_book(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            form = AddBookForm()
        else:
            book = Book.objects.get(id=pk)
            form = AddBookForm(instance=book)
        context = {'form': form}
        return render(request, 'add_book.html', context)
    else:
        if pk == 0:
            form = AddBookForm(request.POST)
        else:
            book = Book.objects.get(id=pk)
            form = AddBookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
    return redirect('book')

def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('book')