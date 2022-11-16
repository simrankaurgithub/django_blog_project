from django.shortcuts import render ,HttpResponseRedirect
from blogapp.models import Category

def nav(request):
    blog= Category.objects.all()
    return {'category' : blog}
