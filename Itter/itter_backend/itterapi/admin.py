from django.contrib import admin

from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin

from .models import UserProfile, Post, Like, Follow

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@admin.register(Like)
class LikeAdmin(ModelAdmin):
    list_display = ['user', 'post', 'created_at']

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ['user', 'content', 'media_url', 'created_at']

@admin.register(Follow)
class FollowAdmin(ModelAdmin):
    list_display = ['follower', 'followee']

@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    list_display = ['user', 'bio','profile_image', 'created_at', 'bio']
