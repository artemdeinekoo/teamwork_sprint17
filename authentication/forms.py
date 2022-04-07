from django import forms
from django.forms import ModelForm
from .models import *
from authentication.models import CustomUser

class AddUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'password', 'role']


    labels = {
        'first_name': 'First Name',
        'middle_name': 'Middle Name',
        'last_name': 'Last Name',
        'email': 'email Name',
        'password': 'password',
        'role': 'Role'
    }

    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)
