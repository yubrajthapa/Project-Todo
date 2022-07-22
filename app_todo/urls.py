
from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard/', views.home_page),
    path('users/register/', views.user_register, name = 'user_register'),
    path('users/login', views.user_login, name = 'user_login'),
]
