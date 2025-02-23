"""
URL configuration for itter_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
import rest_framework.urls
from . import views
from .feeds import PostFeed
from rest_framework import routers
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()

router.register(r'userprofile', views.UserProfileViewSet)
router.register('users', views.UserViewSet, basename='user')
router.register('posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('', views.default_index, name='index'),
    path('0', include(router.urls)),
    path('create/post', views.create_post, name='create_post'),
    path('set-csrf-token', views.set_csrf_token, name='set_csrf_token'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('user', views.user, name='user'),
    path('create-user/', views.create_user_and_profile, name='create_user_and_profile'),
    path('feed/', views.get_feed, name='post-feed'),
    path('post/detail/<pk>', views.get_post_details, name='post_details'),
    path('like/post/', views.update_like, name='update_like'),
    path('user/detail/<username>', views.get_user, name='get_user'),
    path('user/follow/<username>', views.follow_user, name='follow_user'),
    path('verify-email/<str:token>', views.verify_email, name='verify_email'),
    path('test-mail/', views.test_mail, name='send_test_email'),
    
]