from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import RequestContext
from rest_framework.response import Response

import order
from author.models import Author
from book.models import Book
from authentication.models import CustomUser
from order.models import Order
from itertools import chain
from .forms import AddOrderForm
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import OrderSerializer


class OrdersAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderAPIView(APIView):
    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def delete(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk):
        order = Order.objects.get(pk=pk)
        data = request.data
        serializer = OrderSerializer(instance=order, data=data, partial=True)
        if serializer.is_valid():
            order = serializer.save()
            return Response(status=status.HTTP_200_OK)


def order_list(request):
    orders_l = {'orders': Order.objects.all().select_related('book', 'user')}

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
