from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home),
    path('north_indian/', views.north_indian_menu, name = 'north_indian'),
    path('south_indian/', views.south_indian_menu, name = 'south_indian'),
    path('chinese/', views.chinese, name = 'chinese'),
    path('drinks/', views.drinks, name = 'drinks'),


]
