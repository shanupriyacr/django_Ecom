from django.contrib import admin

# Register your models here.
from shop.models import Category,Product

#admin module in Django provides a user interface for managing and editing data in the Django application.
class Categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,Categoryadmin)


class Productadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'slug','price','stock','available','created','updated']

admin.site.register(Product,Productadmin)



