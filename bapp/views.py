from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from . models import *
from django.contrib import messages
from .models import Category, Post
from django.contrib.auth.models import User 

# Create your views here.
def home(request):
    #load all the post from db
    
    posts=Post.objects.all()
    cats=Category.objects.all()
    data={
        'posts':posts,
        'cats':cats 
    }
    return render(request,'home.html',data)
def post(request,url):
    post=Post.objects.get(url=url)
    cats=Category.objects.all()
    
    return render(request,'post.html',{'post':post,'cats':cats})
def category(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    return render(request,'category.html',{'cat':cat,'posts':posts})

#for signup
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password != password2:
            messages.info(request, "Password is not Matching")
            return redirect('/signup/')

        try:
            if User.objects.get(username=username):
                messages.warning(request, "User name  is already Taken")
                return redirect('/signup/')

        except Exception as identifier:
            pass

        user = User.objects.create_user(
            username=username, password=password)
        user.save()
        messages.success(request, "User is Created Please Login")
        # login(request, user)
        return redirect('/login/')  # Redirect to your home page

    return render(request, 'signup.html')

# for user login


def sys_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,
                            username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/login/')

    return render(request, 'login.html')

# for logout


def handleLogout(request):
    logout(request)
    messages.success(request, "Logout Success")
    return redirect('/')
