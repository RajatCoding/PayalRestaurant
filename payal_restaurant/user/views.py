from django.http import HttpResponse
from django.shortcuts import render,redirect
from user.forms import CustomeUserCreationForm,VerifyOtpForm,CusromerLoginForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
import random
from rest_framework.decorators import api_view 
import requests
from rest_framework.response import Response


# Create your views here.
def home(request):
    return render(request, 'menu_base.html')


def user_profile_home(request):
    return render(request, 'profile.html')
    
def user_profile(request):
    return render(request, 'profile.html')

def login_user(request):
    if request.method == 'POST':
        form = CusromerLoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username= uname, password=password)
            if user is not None:
                login(request, user)
                return redirect(user_profile)

    else:
        form = CusromerLoginForm()
    return render(request, 'login.html', {'form':form})

def logout_user(request):
    logout(request)
    return redirect(login_user)

def send_otp(phone_no):
    api_key = '82bd6b1b-125c-11ed-9c12-0200cd936042'
    otp = random.randint(1000,9999)
    # url = f"https://2factor.in/API/V1/{api_key}/SMS/{phone_no}/{otp}"
    # response = requests.get(url)
    return otp

def signup_user(request):
    if request.method == 'POST':
        global forma
        forma = CustomeUserCreationForm(request.POST)
        if forma.is_valid():
            phone_number = forma.cleaned_data['mobile_no']
            global otp
            otp = send_otp(phone_number)
            print(otp)
            messages.success(request, 'Otp has been sent to your mobile n.o')
         
            return redirect(verify_otp)
    else:
        forma = CustomeUserCreationForm()

    return render(request,'signup.html', {'form':forma})

def verify_otp(request):
                if request.method == 'POST':
                    form = VerifyOtpForm(request.POST)
                    if form.is_valid():
                        otp_value = form.cleaned_data['Otp']
                        if otp_value == otp:
                            print("form saved")
                            forma.save()
                            messages.success(request, 'You are registered successfully')
                            return redirect(login_user)
                        else:
                            return redirect(signup_user)

                else:
                    form = VerifyOtpForm()
                    return render(request, 'verify_otp.html', {'form':form})
