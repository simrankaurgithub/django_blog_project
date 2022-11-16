from django.shortcuts import render ,HttpResponseRedirect
from django.urls import is_valid_path
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import Register_form ,login_form 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def blog():
    category=Category.objects.all()
    blog=[]
    for i in category:
        present=Post.objects.filter(category_id=i.pk)
        if present.exists():
            blog.append(Category.objects.all().get(id=i.pk))
    return blog


def home (request):
    blogs=blog()
    post= Post.objects.all().order_by("-updated_at")[:9]
    return render(request, 'blogapp/home.html', {'post' : post, 'blogs' : blogs})


def category (request , slug):
    category= Category.objects.get(slug=slug)
    cats=Post.objects.all().filter(category_id=category).order_by("-updated_at")
    return render(request, 'blogapp/category.html', {'cats' : cats })

def all_blogs (request ):
    posts= Post.objects.all().order_by("-updated_at")
    print(posts)
    return render(request, 'blogapp/all_blogs.html', {'posts' : posts })
    
def detail (request , slug):
    print (slug)
    post= Post.objects.get(slug=slug)
    return render(request, 'blogapp/detail.html',{'post':post})


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


def user_login (request):
    if request.method=='POST':
        fm=login_form(request=request, data= request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Logged in succesfully !')
            return HttpResponseRedirect('/')          
        else:
            try:    
                user=authenticate(username=CustomUsers.objects.get(email=username) ,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in succesfully !')
                    return HttpResponseRedirect('/')
            except:
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in succesfully !')
                    return HttpResponseRedirect('/')   
                else :
                    messages.error(request,'Inavalid Credentials')
                    return HttpResponseRedirect('/login/')  

    fm = login_form()
    return render(request, 'blogapp/login.html',{'form' : fm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def profile(request,username):
    profile=CustomUsers.objects.get(username=username)
    return render(request, 'blogapp/profile.html',{'profile':profile})

def terms (request):
    return render(request, 'blogapp/terms.html')

def policy (request):
    return render(request, 'blogapp/policy.html')

def about (request):
    return render(request, 'blogapp/about.html')
