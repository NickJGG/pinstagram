"""pinstagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.list import ListView

from . import views
from accounts import views as acc_views

urlpatterns = [
    path('', views.index.as_view(), name = 'main'),
    path('upload', views.Upload.as_view(), name = 'upload'),
    path('<str:username>/', acc_views.Profile.as_view(), name = 'profile'),
    path('<str:username>/b', acc_views.Boards.as_view(), name = 'profile_boards'),
    path('<str:username>/follow', views.follow, name = 'follow_user'),
    path('<int:post_id>/like', views.like, name = 'like'),
    path('<int:post_id>/comment', views.CommentV.as_view(), name = 'comment'),
    path('p/<int:post_id>', views.PostV.as_view(), name = "post"),
    path('pin/<int:post_id>', views.PinV, name = 'pin'),
    path('<int:comment_id>/delete', views.DeleteComment, name = 'delete_comment'),
]
