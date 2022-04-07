from django.urls import path
from order import views

urlpatterns = [
    path("", views.order_list, name='all-order'),
    path("delete-order/<int:pk>/", views.delete_order, name='delete-order'),
    path("add-order/", views.add_order, name='add-order'),
    path("update-order/<int:pk>/", views.add_order, name='update-order'),
]