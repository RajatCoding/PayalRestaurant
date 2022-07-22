
from distutils.command.upload import upload
from django.db import models


# Create your models here.

class Shef(models.Model):
    shef_id = models.IntegerField()
    shef_name = models.CharField(max_length=5)


class Category(models.Model):
    Dish_Category = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.Dish_Category
    

class Menu(models.Model):
    Dish_Name = models.CharField(max_length=30)
    Dish_Image = models.ImageField(upload_to = 'DishesImage/')
    Dish_Price = models.IntegerField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    Dish_SubCategory = models.CharField(max_length=60, null=True, blank=True)



    



    
