from django.shortcuts import render
from . models import Menu,Category


# Create your views here.

def home(request):
    return render(request, 'Base.html')


def north_indian_menu(request):
    id = Category.objects.get(Dish_Category='North Indian')
    foods = Menu.objects.filter(Category=id)
    return render(request, 'north_indian.html', {'foods':foods})

def south_indian_menu(request):
    id = Category.objects.get(Dish_Category='South Indian')
    foods = Menu.objects.filter(Category=id)
    return render(request, 'south_indian.html', {'foods':foods})

def chinese(request):
    id = Category.objects.get(Dish_Category='Chinese')
    foods = Menu.objects.filter(Category=id)
    return render(request, 'chinese.html', {'foods':foods})

def drinks(request):
    id = Category.objects.get(Dish_Category='Drinks')
    foods = Menu.objects.filter(Category=id)
    return render(request, 'drinks.html', {'foods':foods})
