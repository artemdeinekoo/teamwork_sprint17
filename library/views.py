from django.utils.timezone import datetime
from django.http import HttpResponse
from library import test_data
from django.shortcuts import render

def main_page(request):
    return render(request, 'main.html')
