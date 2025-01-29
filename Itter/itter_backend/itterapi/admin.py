from django.contrib import admin
from .models import UserProfile, Post, Like, Follow


class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at']
    
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'media_url', 'created_at']
    
class FollowAdmin(admin.ModelAdmin):
    list_display = ['follower', 'following']
    
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio','profile_image', 'created_at', 'bio']

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Like, LikeAdmin)
admin.site.register(Follow)