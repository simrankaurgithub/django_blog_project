from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class post (models.Model):
    title=models.CharField(max_length=200)
    slug = models.CharField(max_length = 200)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    image = models.ImageField(upload_to ='uploads/')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
