from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Base.html')


def north_indian_menu(request):
    return render(request, 'north_indian.html')
