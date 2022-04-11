"""djangoViewTemplates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from library import views
from authentication.views import CustomUsersAPIView, CustomUserAPIView  
from author.views import AuthorsAPIView, AuthorAPIView
from book.views import BooksAPIView, BookAPIView
from order.views import OrdersAPIView, OrderAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
    path("author/", include("author.urls")),
    path("user/", include("authentication.urls")),
    path("order/", include("order.urls")),
    path('', include('book.urls')),
    path('api/v1/user', CustomUsersAPIView.as_view()),
    path('api/v1/user/<int:pk>', CustomUserAPIView.as_view()),
    path('api/v1/author', AuthorsAPIView.as_view()),
    path('api/v1/author/<int:pk>', AuthorAPIView.as_view()),
    path('api/v1/book', BooksAPIView.as_view()),
    path('api/v1/book/<int:pk>', BookAPIView.as_view()),
    path('api/v1/order', OrdersAPIView.as_view()),
    path('api/v1/order/<int:pk>', OrderAPIView.as_view()),
]
