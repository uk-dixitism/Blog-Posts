from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def index(request):
    posts = Post.objects.all()
    username = request.user.get_username()
    return render(request, 'index.html',{'posts': posts, 'username': username})

@login_required(login_url="login")
def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})

@login_required(login_url="login")
def delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('http://127.0.0.1:8000/index')

@login_required(login_url="login")
def create(request):
    username = request.user.get_username()
    return render(request, 'create.html', {'username':username}) 

@login_required(login_url="login")
def create2(request):
    if request.method=='POST':
        post=Post()
        post.title= request.POST.get('title')
        post.body= request.POST.get('content')
        post.username=request.POST.get('username')
        post.save()
    return redirect('http://127.0.0.1:8000/index')

@login_required(login_url="login")
def edit(request, pk):
    post = Post.objects.get(id=pk)
    title = post.title
    body = post.body
    id = post.id
    username = request.user.get_username()
    return render(request, 'edit.html', {'title' : title, 'body': body, 'id': id, 'username': username})

@login_required(login_url="login")
def edit2(request, pk):
    if request.method=='POST':
        post = Post.objects.get(id=pk)
        post.title= request.POST.get('title')
        post.body= request.POST.get('body')
        post.username= request.POST.get('username')
        post.save()
    return redirect('http://127.0.0.1:8000/index')

def login(request):
    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if(user is None):
            messages.info(request, 'Invalid login credentials')
            return redirect('/')
        else:
            auth.login(request,user)
            return redirect('index')
    else:
        return render(request, 'login.html')

def register(request):
    if(request.method=='POST'):
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
    
        if(password==password2):
            if(User.objects.filter(email=email).exists()):
                messages.info(request, 'Email already used')
                return redirect('register')
            elif(User.objects.filter(username=username).exists()):
                messages.info(request, 'Username is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('/')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    messages.info(request, 'You have been logged out successfully')
    return redirect('/')