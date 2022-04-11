from django.urls import path
from xml.etree.ElementInclude import include
from library import views
from .views import *
from book import views

urlpatterns = [
    path('', views.book_list, name='book'),
    path('book/<int:id>/', specificBook),
    path('book/unordered-books/', unorderedBook),
    path('book/unordered-books/<int:id>/', specificBook),
    path('book/add_book/', views.add_book, name='add_book'),
    path('update_book/<int:pk>/',  views.add_book, name='update_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]