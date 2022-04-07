from django import forms
from django.forms import ModelForm
from .models import *
from author.models import Author

class AddAuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']


    def __init__(self, *args, **kwargs):
        super(AddAuthorForm, self).__init__(*args, **kwargs)
