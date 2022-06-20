from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('add/post/', views.addblog, name='addblog'),
    path('', views.login_view, name='login'),
]