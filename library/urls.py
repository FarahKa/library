"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from inventory import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import include

#router = DefaultRouter()
#router.register(r'books', views.BookViewSet, basename = 'book')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name="authors"),
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view(), name="books"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('percentage/<int:pk>/', views.percentage_read, name='percentage'),
    path('', include('django_prometheus.urls')),
    path('', views.health_check),
] 
#+ router.urls
