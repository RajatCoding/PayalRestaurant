from django.contrib import admin
from . models import Menu,Category

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ['Dish_Name','Dish_Image','Dish_Price', 'Category']

admin.site.register(Menu, MenuAdmin)
admin.site.register(Category,admin.ModelAdmin)
