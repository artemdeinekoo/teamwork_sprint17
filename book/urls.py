from django.urls import path

from library import views
from .views import *


urlpatterns = [
    path('book/', book, name='book'), 
    path('book/<int:id>/', specificBook),
    path('book/unordered-books/', unorderedBook),
    path('book/unordered-books/<int:id>/', specificBook),
    path('book/add_book/', add_book, name='add_book'),
    path('update_book/<int:pk>/', add_book, name='update_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]