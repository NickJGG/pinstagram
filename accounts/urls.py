from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = '../login/'), name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('edit', views.EditProfile.as_view(), name = "edit_profile"),
    path('edit/pic/<int:post_id>', views.changeProfPic, name = 'change_pic'),
]
