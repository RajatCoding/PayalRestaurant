from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from user.models import CustomUser

class CustomeUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=("Password"),
        
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        help_text=None,
        required=True
        )
    password2 = forms.CharField(
        label=("Confirm Password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        help_text=None
        )
   

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','mobile_no', 'email', 'address']

        widgets = {
        'first_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter First Name'}),

        'last_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Last Name'}),

        'mobile_no': forms.TextInput(attrs = {'class':'form-control','placeholder':'Mobile Number'}),

        'email': forms.EmailInput(attrs = {'class':'form-control','placeholder':'Enter your email','required':'true'}),

        'address': forms.Textarea(attrs = {'class':'form-control','placeholder':'Enter your address','rows':4}),
        }

class VerifyOtpForm(forms.Form):
     Otp = forms.IntegerField()

class CusromerLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label=("Email Id"),
        
        widget=forms.EmailInput(attrs={'class':'form-control'}),
        help_text=None,
        required=True
        )
    password = forms.CharField(
        label=("Password"),
        
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        help_text=None,
        required=True
        )
    class Meta:
        model = CustomUser
        fields = '__all__'
        
        
        
