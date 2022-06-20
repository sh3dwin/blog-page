from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import BlogPost, BlogForm, BlogUser
from django import forms
import django.utils.timezone

# Create your views here.

def posts(request):
    blogs = BlogPost.objects.all()
    current_user = request.user
    return render(request, 'posts.html', {"blogs": blogs})

def addblog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('posts')
    else:
        form = BlogForm()
    return render(request,
            'add/posts.html',
            {'form': form})