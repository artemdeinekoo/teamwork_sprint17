from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from author.forms import AddAuthorForm
from author.models import Author
from book.models import Book

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
