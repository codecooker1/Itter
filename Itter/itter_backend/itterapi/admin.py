from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import UserProfile, Post, Like, Follow


class LikeAdmin(ModelAdmin):
    list_display = ['user', 'post', 'created_at']
    
class PostAdmin(ModelAdmin):
    list_display = ['user', 'content', 'media_url', 'created_at']
    
class FollowAdmin(ModelAdmin):
    list_display = ['follower', 'following']
    
class UserProfileAdmin(ModelAdmin):
    list_display = ['user', 'bio','profile_image', 'created_at', 'bio']

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Like, LikeAdmin)
admin.site.register(Follow)