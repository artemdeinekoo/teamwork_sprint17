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
from .forms import AddUserForm

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


# def update_user(request, pk):
#     user = CustomUser.objects.get(id=pk)
#     form = AddUserForm(instance=user)
#     if request.method == 'POST':
#         form = AddUserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('all-user')
#     context = {'form': form}
#     return render(request, 'add_user.html', context)
#     if request.method == 'GET':
#         form = AddUserForm(request.GET, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('all-user')
#     context = {'form': form}
#     return render(request, 'add_user.html', context)





# def update_user(request, id):
#     user = CustomUser.objects.get(pk=id)
#     form = AddUserForm(instance=user)
#     if request.method == 'POST':
#         form = AddUserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('all-user')
#     # else:
#     #     user = CustomUser.objects.get(pk=id)
#     #     form = AddUserForm(instance=user)
#     context = {'form': form}
#     return render(request, 'add_user.html', context)
#     # return render(request, 'add_user.html')

# def delete(request):
#     if request.method == 'POST':
#         form = DelUserForm(request.POST)
#         if form.is_valid():
#             user_id = form.cleaned_data["user_id"]
#         else:
#             form = DelUserForm()
#         return render(request, 'add_user.html', {'form': form, 'title': 'Add information about user'})


# def delete(request, id):
#     try:
#         user = CustomUser.objects.get(id=id)
#         user.delete()
#         return render(request, 'add_user.html')
#     except CustomUser.DoesNotExist:
#         return HttpResponseNotFound("<h2>User not found</h2>")


# def add_user(request):
#         if request.method == 'POST':
#             form = AddUserForm(request.POST)
#             if form.is_valid():
#                 try:
#                     form.save()
#                     return redirect('add-user')
#                 except:
#                     form.add_error(None, 'Error during save to DB. Please, check input data')
#         else:
#             form = AddUserForm()
#         return render(request, 'add_user.html', {'form': form, 'title': 'Add information about user'})
