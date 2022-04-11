from django.shortcuts import render, redirect
from .models import *
from order.models import Order
from .forms import AddBookForm
from book.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class BooksAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookAPIView(APIView):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk):
        book = Book.objects.get(pk=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid():
            book = serializer.save()
            return Response(status=status.HTTP_200_OK)


def book_list(request, sorted="asc"):
    if sorted == "asc":
        book_list = {'book': Book.objects.all().order_by("name"), 'sorted': "desc"}
    else:
        book_list = {'book': Book.objects.all().order_by("-name"), 'sorted': "asc"}

# def home(request):
#     return render(request, 'main.html')
#
# def book(request):
#     books = Book.get_all()
#     return render(request, 'book.html', {'books' : books})
#
# def specificBook(request, id):
#     specificBook = Book.get_by_id(id)
#     return render(request, 'bookById.html', {'specificBook' : specificBook})
#
# def unorderedBook(request):
#     all_books = Book.objects.all()
#     all_orders = Order.objects.all()
#     orders_book_ids = []
#     for order in all_orders:
#         orders_book_ids.append(order.book.pk)
#
#     unordered_books = []
#
#     for book in all_books:
#         if book.id not in orders_book_ids:
#             unordered_books.append(book)
#         else:
#             continue
#     return render(request, 'unorderedBooks.html', {'unordered_books' : unordered_books})
#
# def add_book(request, pk=0):
#     if request.method == 'GET':
#         if pk == 0:
#             form = AddBookForm()
#         else:
#             book = Book.objects.get(id=pk)
#             form = AddBookForm(instance=book)
#         context = {'form': form}
#         return render(request, 'add_book.html', context)
#     else:
#         if pk == 0:
#             form = AddBookForm(request.POST)
#         else:
#             book = Book.objects.get(id=pk)
#             form = AddBookForm(request.POST, instance=book)
#     if form.is_valid():
#         form.save()
#     return redirect('book')
#
# def delete_book(request, pk):
#     book = Book.objects.get(id=pk)
#     book.delete()
#     return redirect('book')
