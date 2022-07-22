from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Base.html')


def north_indian_menu(request):
    return render(request, 'north_indian.html')

def south_indian_menu(request):
    return render(request, 'south_indian.html')

def chinese(request):
    return render(request, 'chinese.html')

def drinks(request):
    return render(request, 'drinks.html')
