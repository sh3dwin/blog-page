from django.contrib import admin

# Register your models here.

from .models import BlogUser, BlogPost, Comment

admin.site.register(BlogUser)
admin.site.register(BlogPost)
admin.site.register(Comment)