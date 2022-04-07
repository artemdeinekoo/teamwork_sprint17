from django.urls import path
from author import views

urlpatterns = [
    path("", views.author_list, name = 'author'),
    path("sorting/<str:sorted>/", views.author_list),
    path("<int:id>/", views.author_about),
    path("add_author/", views.add_author,  name = 'add_author'),
    path("update_author/<int:pk>/", views.add_author,  name = 'update_author'),
    path("delete_author/<int:pk>/", views.delete_author, name='delete_author'),
]