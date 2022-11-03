from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

class CustomUsers(AbstractUser):
    email = models.EmailField(blank=False , unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    status = models.BooleanField(default=True)
    
        


class posts (models.Model):
    title=models.CharField(max_length=200)
    slug = models.CharField(max_length = 200)
    author = models.ForeignKey(CustomUsers, on_delete= models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    image = models.ImageField(upload_to ='uploads/')
    content = models.TextField()
    status = models.BooleanField(default=True)
