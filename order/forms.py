from django import forms
from django.forms import ModelForm
from .models import *
from order.models import Order
import datetime

class AddOrderForm(forms.ModelForm):
    plated_end_at = forms.DateTimeField(initial=datetime.datetime.now() + datetime.timedelta(days=17))
    class Meta:
        model = Order
        fields = ['plated_end_at','user','book']


    labels = {
        'user' : 'User of library',
        'book' : 'Book from library',
        'plated_end_at' : 'Planned date of return',
    }

    def __init__(self, *args, **kwargs):
        super(AddOrderForm, self).__init__(*args, **kwargs)
        self.fields['user'].label_from_instance = lambda obj: f'{obj.id} {obj.first_name} {obj.last_name}'
        self.fields['book'].label_from_instance = lambda obj: f'{obj.id} {obj.name}'
