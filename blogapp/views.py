from django.shortcuts import render ,HttpResponseRedirect
from django.urls import is_valid_path
from .models import posts
from django.contrib.auth.forms import UserCreationForm
from .forms import Register_form ,login_form
from django.contrib import messages

# Create your views here.
def home (request):
    blog= posts.objects.all()
    return render(request, 'blogapp/home.html', {'post' : blog})

def register (request):
    if request.method == 'POST':
        fm =Register_form (request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request ,"Account created successfuly !")
            return HttpResponseRedirect("/login/") 
    else:  
        fm = Register_form ()
    return render(request, 'blogapp/registration.html', {'form' : fm})


def login (request):
    fm = login_form()
    return render(request, 'blogapp/login.html',{'form' : fm})

def blogs (request):
    return render(request, 'blogapp/blog.html')

def terms (request):
    return render(request, 'blogapp/terms.html')

def policy (request):
    return render(request, 'blogapp/policy.html')

def about (request):
    return render(request, 'blogapp/about.html')
