from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from author.forms import AddAuthorForm
from author.models import Author
from book.models import Book
from author.serializers import AuthorSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status




class AuthorsAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class AuthorAPIView(APIView):
    def get(self, request, pk):
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def delete(self, request, pk):
        author = Author.objects.get(pk=pk)
        author.delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk):
        author = Author.objects.get(pk=pk)
        data = request.data
        serializer = AuthorSerializer(instance=author, data=data, partial=True)
        if serializer.is_valid():
            author = serializer.save()
            return Response(status=status.HTTP_200_OK)


def author_list(request, sorted="asc"):
    if sorted=="asc":
        author_list={'authors': Author.objects.all().order_by("name"), 'sorted': "desc"}
    else: author_list={'authors': Author.objects.all().order_by("-name"), 'sorted': "asc"}

    return render(request, 'author-list.html', author_list)

def author_about(request, id):

    author_about={'author': Author.objects.get(id=id), 'books': Book.objects.filter(authors=id)}

    return render(request, 'author-about.html', author_about)

def add_author(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            form = AddAuthorForm()
        else:
            author = Author.objects.get(id=pk)
            form = AddAuthorForm(instance=author)
        context = {'form': form}
        return render(request, 'add_author.html', context)
    else:
        if pk == 0:
            form = AddAuthorForm(request.POST)
        else:
            author = Author.objects.get(id=pk)
            form = AddAuthorForm(request.POST, instance=author)
    if form.is_valid():
        form.save()
    return redirect('author')

def delete_author(request, pk):
    author = Author.objects.get(id=pk)
    author.delete()
    return redirect('author')
