from django.urls import path
from order import views

urlpatterns = [
    path("", views.order_list, name='order'),
    path("sorting/<str:sorted>/", views.order_list),
    path("add_order/", views.add_order, name='add_order'),
    path("delete_order/<int:pk>/", views.delete_order, name='delete_order'),
    path("update-order/<int:pk>/", views.add_order, name='update-order'),
]