from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

class CustomUsers(AbstractUser):
    email = models.EmailField(blank=False , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    first_name = models.CharField(max_length=255,blank =False)
    # phone_number = models.CharField(max_length=12 , default='')
    # address= models.TextField(default='')


class Category(models.Model):
    name=models.CharField(max_length=200)
    slug = models.SlugField(max_length = 200, blank=True)
    image = models.ImageField(upload_to ='category/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Post (models.Model):
    title=models.CharField(max_length=200)
    slug = models.SlugField(max_length = 200 ,blank=True)
    category_id = models.ForeignKey(Category, on_delete= models.CASCADE)
    author = models.ForeignKey(CustomUsers, on_delete= models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now= True)
    image = models.ImageField(upload_to ='uploads/')
    content = RichTextField()
        
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)