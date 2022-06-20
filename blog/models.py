from datetime import datetime
from django.db import models
from django.contrib.auth.models import User, UserManager
from django import forms
import django.utils.timezone
from django.forms import TextInput
# Create your models here.

class BlogUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self) -> str:
        return self.user.username


class BlogPost(models.Model):
    title = models.CharField(max_length=10)
    author = models.ForeignKey(BlogUser, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    files = models.FileField(blank=True)
    publication_date = models.DateTimeField('Date published', default=django.utils.timezone.now)
    edited_last = models.DateTimeField('Last edited', default=django.utils.timezone.now)

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'user': TextInput(attrs={'readonly': 'readonly'})
        }

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    blog_user = models.ForeignKey(BlogUser, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField('Commented at')
    body = models.TextField(default='')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['blog_post', 'date'], name='unique_post_date_combination'
            )
        ]


