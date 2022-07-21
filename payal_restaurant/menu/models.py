from django.db import models


# Create your models here.

class Shef(models.Model):
    shef_id = models.IntegerField(max_length=5)
    shef_name = models.CharField(max_length=5)

class Menu(models.Model):
    Dish_Name = models.CharField(max_length=30)
    Dish_Quantity = models.IntegerField()


    
