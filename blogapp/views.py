from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import JsonResponse
from django.urls import is_valid_path
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
import re
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def blog():
    category = Category.objects.all().order_by('-updated_at').order_by('name')
    blog = []
    for i in category:
        present = Post.objects.filter(category_id=i.pk)
        if present.exists():
            blog.append(Category.objects.all().get(id=i.pk))
    return blog


def home(request):
    blogs = blog()
    print(blogs)
    post = Post.objects.all().order_by("-updated_at")[:9]
    return render(request, 'blogapp/home.html', {'post': post, 'blogs': blogs})


def category(request, slug):
    category = Category.objects.get(slug=slug)
    category1 = Category.objects.all().get(slug=slug)
    cats = Post.objects.filter(category_id=category).order_by("-updated_at")
    blogs = blog()
    return render(request, 'blogapp/category.html', {'cats': cats,  'blogs': blogs, 'category':category1})


def all_blogs(request):
    blogs = blog()
    posts = Post.objects.all().order_by("-updated_at")
    return render(request, 'blogapp/all_blogs.html', {'posts': posts, 'blogs': blogs})


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    blogs = blog()
    return render(request, 'blogapp/detail.html', {'post': post, 'blogs': blogs})


def register(request):
    blogs = blog()
    if request.method == 'POST':
        fm = Register_form(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Account created successfuly !")
            return HttpResponseRedirect("/login/")
    else:
        fm = Register_form()
    return render(request, 'blogapp/registration.html', {'form': fm, 'blogs': blogs})


def user_login(request):
    blogs=blog()
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = login_form(request=request, data=request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in succesfully !')
                return HttpResponseRedirect('/')
            else:
                try:
                    user = authenticate(username=CustomUsers.objects.get(
                        email=username), password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, 'Logged in succesfully !')
                        return HttpResponseRedirect('/')
                except:
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, 'Logged in succesfully !')
                        return HttpResponseRedirect('/')
                    else:
                        messages.error(request, 'Inavalid Credentials')
                        return HttpResponseRedirect('/login/')
        fm = login_form()
        return render(request, 'blogapp/login.html', {'form': fm, 'blogs': blogs})


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out succesfully !')
    return HttpResponseRedirect('/')


def profile(request, username):
    blogs = blog()
    profile = CustomUsers.objects.get(username=username)
    return render(request, 'blogapp/profile.html', {'profile': profile, 'blogs': blogs})


def edit_profile(request, username):
    blogs = blog()
    user = CustomUsers.objects.get(username=username)
    if request.method == 'POST':
        fm = Register_form(request.POST)
        first_name = request.POST['first_name']
        print(first_name)
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        try:
            user.image = request.FILES['image']
        except:
            pass
        user.save()
        if ((re.match("^[a-zA-Z]+$", first_name))):
            if(((phone_number == "") or (re.match("^[0-9]{10}$", phone_number))) and ((last_name == "") or (re.match ("^[a-zA-Z]+$",last_name)))):
                CustomUsers.objects.filter(username=username).update(first_name=first_name, last_name=last_name, phone_number=phone_number,address=address)
                messages.success(request, "Profile updated successfuly !")
                return HttpResponseRedirect(f"/profile/{username}")
        else:
            messages.error(request, 'Inavalid Credentials')
    else:
        fm = Register_form(instance = user)
    return render(request, 'blogapp/edit_profile.html', {'form': fm, 'blogs': blogs})


def add_blog(request):
    blogs = blog()
    if request.method == 'POST':
        add_form=Post_form(request.POST)
    else:
        add_form=Post_form()    
    return render(request, 'blogapp/add_blog.html', {'blogs': blogs, 'add_form':add_form})


def check_user_exist(request):
    username = request.GET.get('username')
    check = CustomUsers.objects.filter(username=username)
    if len(check) == 0:
        return JsonResponse({"status": 0, "message": "not exist"})
    else:
        return JsonResponse({"status": 1, "message": "Exist"})


def check_email_exist(request):
    email = request.GET.get('email')
    check = CustomUsers.objects.filter(email=email)
    if len(check) == 0:
        return JsonResponse({"status": 0, "message": "not exist"})
    else:
        return JsonResponse({"status": 1, "message": "Exist"})


def terms(request):
    blogs = blog()
    return render(request, 'blogapp/terms.html', {'blogs': blogs})


def policy(request):
    blogs = blog()
    return render(request, 'blogapp/policy.html',  {'blogs': blogs})


def about(request):
    blogs = blog()
    return render(request, 'blogapp/about.html',  {'blogs': blogs})
