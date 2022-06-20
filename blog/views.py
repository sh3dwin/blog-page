from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import BlogPost, BlogForm, BlogUser, BlogUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django import forms
import django.utils.timezone

# Create your views here.

def posts(request):
    blogs = BlogPost.objects.all()
    return render(request, 'posts.html', {"blogs": blogs})


def addblog(request):
    if not request.user.is_authenticated:
        return redirect(login_view)
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form = form.save(commit='False')
            form.author = request.user
            form = form.save()
            return redirect('posts')
    else:
        form = BlogForm()
    return render(request,
            'add/posts.html',
            {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(user)
            return redirect('posts')
        else:
            error = "Username or password is incorrect."
    else:
        error = "Something went wrong."
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'error': error})
