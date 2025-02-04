from django.contrib import admin

from unfold.admin import ModelAdmin

from .models import UserProfile, Post, Like, Follow

admin.site.unregister(UserProfile)
admin.site.unregister(Post)
admin.site.unregister(Like)
admin.site.unregister(Follow)

@admin.register(Like)
class LikeAdmin(ModelAdmin):
    list_display = ['user', 'post', 'created_at']

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ['user', 'content', 'media_url', 'created_at']

@admin.register(Follow)
class FollowAdmin(ModelAdmin):
    list_display = ['follower', 'following']

@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    list_display = ['user', 'bio','profile_image', 'created_at', 'bio']
