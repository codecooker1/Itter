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
from rest_framework import routers
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()

router.register(r'userprofile', views.UserProfileViewSet)

urlpatterns = [
    path('', views.default_index, name='index'),
    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    # path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    path('create/post', views.create_post, name='create_post'),
    path('set-csrf-token', views.set_csrf_token, name='set_csrf_token'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('user', views.user, name='user'),
    path('register', views.register, name='register'),
    path('gettestimg', views.getSampleIcon, name = 'testimg'),
    path('gettestname/<int:user_id>', views.getNameHandle, name = 'testname'),
    path('v0/auth', include('rest_framework.urls')),
    path('v0/', include(router.urls)),
    path('create-user/', views.create_user_and_profile, name='create_user_and_profile'),
    path('tt/', views.test_form, name='test_form'),
]
