from django.urls import path
from authentication import views

urlpatterns = [
    path("", views.user_list,  name = 'all-user'),
    path("<int:id>/", views.user_orders),
    path("add-user/", views.add_user,  name = 'add-user'),
    path("update-user/<int:pk>/", views.add_user,  name = 'update-user'),
    path("delete-user/<int:pk>/", views.delete_user, name='delete-user'),

    #path("del-user/", views.del_user,  name = 'del-user'),
]