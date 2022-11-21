from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','category_id','created_at','updated_at','image']


@admin.register(CustomUsers)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','created_at','updated_at']
 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_at','updated_at']
    