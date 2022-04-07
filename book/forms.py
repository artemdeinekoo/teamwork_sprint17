from django import forms
from django.forms import ModelForm
from .models import *
from book.models import Book

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'authors']

    def __init__(self, *args, **kwargs):
        super(AddBookForm, self).__init__(*args, **kwargs)