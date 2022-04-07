# from multiprocessing import context
# from unicodedata import name
# from django.shortcuts import render
# from author.models import Author
# from book.models import Book
# from order.models import Order

from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import RequestContext
from author.models import Author
from book.models import Book
from authentication.models import CustomUser
from order.models import Order
from itertools import chain
from .forms import AddOrderForm

def order_list(request):

    orders_l={'orders': Order.objects.all().select_related('book','user')} 

    return render(request, 'order-list.html', orders_l)

def add_order(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            form = AddOrderForm()
        else:
            order = Order.objects.get(id=pk)
            form = AddOrderForm(instance=order)
        context = {'form': form}
        return render(request, 'add_order.html', context)
    else:
        if pk == 0:
            form = AddOrderForm(request.POST)
        else:
            order = Order.objects.get(id=pk)
            form = AddOrderForm(request.POST, instance=order)
    if form.is_valid():
        form.save()
    return redirect('all-order')

def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('all-order')
