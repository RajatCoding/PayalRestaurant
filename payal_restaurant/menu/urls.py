from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home),
    path('north_indian/', views.north_indian_menu, name = 'north_indian'),


]
