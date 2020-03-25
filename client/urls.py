#from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('all/', views.all, name='all'),
    path('login/', views.login, name='login'),
    path('logout/', views.login, name='logout'),
]
