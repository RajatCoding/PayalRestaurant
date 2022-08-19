from rest_framework.decorators import api_view    
import random
import requests
from rest_framework.response import Response
        
@api_view    
def send_otp():
        phone_number = 8103382908
        api_key = '82bd6b1b-125c-11ed-9c12-0200cd936042'
        otp = random.randint(1000,9999)
        print(otp)
        url = f"https://2factor.in/API/V1/{api_key}/SMS/{phone_number}/{otp}/"
        header = {}
        payload = {}
        response = requests.get(url, headers=header, data=payload)
        # response = requests.get(url)
        return Response({'msg':'otp sent successfully'})
        # print("otp sent successfully")


alfa = send_otp()
print(alfa)
