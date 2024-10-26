from django.contrib import admin
from .models import UserProfile, Post, Like, Follow

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Follow)