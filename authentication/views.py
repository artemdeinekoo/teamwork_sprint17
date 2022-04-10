from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import RequestContext
from authentication import serializers
from author.models import Author
from book.models import Book
from authentication.models import CustomUser
from order.models import Order
from itertools import chain
from .forms import AddUserForm
from rest_framework.views import APIView
from authentication.serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status


class CustomUsersAPIView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomUserAPIView(APIView):
    def get(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        data = request.data
        serializer = CustomUserSerializer(instance=user, data=data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            return Response(status=status.HTTP_200_OK)



def user_list(request):
    user_l={'users': CustomUser.objects.all()}
    return render(request, 'user-list.html', user_l)

def user_orders(request, id):

    user_order={'user_info': CustomUser.objects.get(id=id), \
        'orders': Order.objects.filter(user=id).select_related('book')} 

    return render(request, 'user-orders.html', user_order)

def add_user(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            form = AddUserForm()
        else:
            user = CustomUser.objects.get(id=pk)
            form = AddUserForm(instance=user)
        context = {'form': form}
        return render(request, 'add_user.html', context)
    else:
        if pk == 0:
            form = AddUserForm(request.POST)
        else:
            user = CustomUser.objects.get(id=pk)
            form = AddUserForm(request.POST, instance=user)
    if form.is_valid():
        form.save()
    return redirect('all-user')

def delete_user(request, pk):
    user = CustomUser.objects.get(id=pk)
    user.delete()
    return redirect('all-user')




