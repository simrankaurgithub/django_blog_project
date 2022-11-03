from django.contrib import admin
from .models import posts , CustomUsers
# Register your models here.
@admin.register(posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','created_on','updated_on','image']


@admin.register(CustomUsers)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','created_on','updated_on']
    