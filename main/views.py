from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.models import User
from pathlib import Path
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
import arrow

from .models import *

class index(ListView):
    model = Post
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            up = UserProfile.objects.filter(user = self.request.user).values('following')
            p = Post.objects.filter(user__in = up).order_by('-date_posted')[:10]

            for post in p:
                post.profile = UserProfile.objects.get(user = post.user)
                
                post.likes = UserProfile.objects.filter(liked_posts = post)
                post.liked = post.likes.filter(user = self.request.user).exists()
                post.comments = Comment.objects.filter(post = post)
                post.posted = arrow.get(post.date_posted).humanize()
                post.pinned = Pin.objects.filter(user = self.request.user, post = post).exists()
            
            context['posts'] = p
        
        return context

class Upload(ListView, ModelFormMixin):
    model = Post
    template_name = 'main/upload.html'
    form_class = PostForm

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            p = Post(user = request.user, image = self.form.cleaned_data['image'], description = '')
            p.save()
        else:
            print("form is not valid")

        # Whether the form validates or not, the view will be rendered by get()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context

def fileExists(username):
    return Path(MEDIA_URL + "img/users/" + username + "/profile.jpg").exists()

def follow(request, username):
    u = User.objects.get(username = username)
    
    up = UserProfile.objects.get(user = request.user)
    fol = up.following.all()

    if u in fol:
        up.following.remove(u)
    else:
        up.following.add(u)

    return HttpResponse('<script>location = "../' + username + '"</script>')

def like(request, post_id):
    print('LIKED POST')
    p = Post.objects.get(id = post_id)
    
    up = UserProfile.objects.get(user = request.user)
    liked = up.liked_posts.all()

    if p in liked:
        up.liked_posts.remove(p)
        return JsonResponse({'like': 'false'})
    else:
        up.liked_posts.add(p)
        return JsonResponse({'like': 'true'})

class CommentV(ListView, ModelFormMixin):
    model = Comment
    form_class = CommentForm
    template_name = 'main/upload.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            #com = Comment(post = Post.objects.get(id = self.kwargs['post_id']), user = request.user, text = self.form.cleaned_data['text'])
            p = Comment(user = request.user, text = self.form.cleaned_data['text'], post = Post.objects.get(id = self.kwargs['post_id']))
            p.save()

            return JsonResponse({'username': request.user.username, 'comment_id': p.id})
        else:
            print("form is not valid")

        
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context

class PostV(ListView):
    model = Post
    template_name = 'main/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        post = Post.objects.get(id = self.kwargs['post_id'])
        post.comments = Comment.objects.filter(post = post)
        post.likes = UserProfile.objects.filter(liked_posts = post)
        post.liked = post.likes.filter(user = self.request.user).exists()
        post.posted = arrow.get(post.date_posted).humanize()
        
        up = UserProfile.objects.get(user = post.user)

        context['post'] = post
        context['profile'] = up
        context['is_user'] = self.request.user == post.user

        if context['is_user']:
            context['is_following'] = post.user in UserProfile.objects.get(user = self.request.user).following.all()
        
        return context

def PinV(request, post_id):
    if request.user.is_authenticated:
        pins = Pin.objects.filter(user = request.user, post = Post.objects.get(id = post_id))

        if pins.exists():
            pins[0].delete()
        else:
            p = Pin(user = request.user, post=Post.objects.get(id = post_id))
            p.save()

    return HttpResponse('')

def DeleteComment(request, comment_id):
    if request.user.is_authenticated:
        c = Comment.objects.get(id = comment_id)
        c.delete()

    return HttpResponse('')