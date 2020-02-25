from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse

from . import create
from main.models import *

def register(request):
    if request.GET.get('submit'):
        if request.GET.get('username') and request.GET.get('password') and request.GET.get('password-confirm') and request.GET.get('email') and request.GET.get('firstname') and request.GET.get('lastname') and request.GET.get('month') and request.GET.get('day') and request.GET.get('year'):
            create.user(request, request.GET.get('username'), request.GET.get('password'), request.GET.get('email'), request.GET.get('firstname'), request.GET.get('lastname'), request.GET.get('month'), request.GET.get('day'), request.GET.get('year'))
            return redirect('../login')
    
    return render(request, 'accounts/register.html')

    return context

def profileInfo(context, username, user):
    u = User.objects.get(username = username)
    p = UserProfile.objects.get(user = u)
    posts = Post.objects.filter(user = u).order_by('-date_posted')

    for post in posts:
        post.likes = UserProfile.objects.filter(liked_posts = post)
        post.comments = Comment.objects.filter(post = post)

    context['posts'] = posts
    context['profile'] = u
    context['profile_info'] = p
    context['is_following'] = u in UserProfile.objects.get(user = user).following.all()

    context['following'] = UserProfile.objects.get(user=u).following.all()
    context['followers'] = UserProfile.objects.filter(following=u)

    return context

class Profile(ListView):
    model = User
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = profileInfo(context, self.kwargs['username'], self.request.user)

        return context

class EditProfile(ListView):
    model = UserProfile
    template_name = "accounts/editprofile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.get(user = self.request.user)
        context['posts'] = Post.objects.filter(user = self.request.user)
        
        return context

class Boards(ListView):
    model = Board
    template_name = 'accounts/pins.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = profileInfo(context, self.kwargs['username'], self.request.user)
        context['boards'] = Board.objects.filter(user = User.objects.get(username = self.kwargs['username']))

        for b in context['boards']:
            b.pins_prev = b.pins.all()[:9]

        return context

def changeProfPic(request, post_id):
    if (request.user.is_authenticated):
        u = UserProfile.objects.get(user = request.user);

        u.prof_post = Post.objects.get(id = post_id)
        u.save()

        print('\n\nCHANGED PROFILE PICTURE\n\n')

    return HttpResponse('')