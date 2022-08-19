from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.core.exceptions import ValidationError
import re
from user.modelmanager import CustomUserManager

def mobile_validate(value):
    val = re.fullmatch("[7-9]\d{9}",value)
    if val == None:
        raise ValidationError("Enter valid mobile number. should startwith(7,8,9) and contain 10digits")



class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    mobile_no = models.CharField(null= True,blank=False,max_length=10,unique=True, validators=[mobile_validate])
    email = models.EmailField(_('email address'), unique=True)
    address = models.CharField(max_length=200,blank=False )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name',]

    objects = CustomUserManager()

    def __str__(self):
        return self.email




   