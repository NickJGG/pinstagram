from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime

from .storage import OverwriteStorage

def getDir(instance, filename):
    ext = filename.split('.')[-1]

    return 'img/users/{0}/{1}'.format(instance.user.username, filename)

def getProDir(instance, filename):
    return 'img/users/{0}/{1}'.format(instance.user.username, filename)

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = getDir)
    description = models.CharField(max_length = 1000, default = '')
    date_posted = models.DateTimeField(auto_now_add = True, blank = True)

class Comment(models.Model):
    id = models.AutoField(primary_key = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.CharField(max_length = 1000)
    date_posted = models.DateTimeField(auto_now_add = True, blank = True)

class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name = 'user', on_delete = models.CASCADE, primary_key = True)
    liked_posts = models.ManyToManyField(Post, related_name = 'liked_posts')
    following = models.ManyToManyField(User, related_name = 'user_following')
    prof_post = models.ForeignKey(Post, related_name = 'profile_picture', on_delete = models.CASCADE, blank = True, null = True)
    description = models.CharField(max_length = 280)
    dob = models.DateField(default = datetime.date.today)

class Pin(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    tags = models.TextField()

    class Meta:
        unique_together = (('user', 'post'),)

class Board(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    pins = models.ManyToManyField(Post, blank = True)

    class Meta:
        unique_together = (('user', 'name'),)

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']