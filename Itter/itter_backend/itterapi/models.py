from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField()

class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    media_url = models.URLField()
    created_at = models.DateTimeField()

# class Repost(models.Model):
#     pass

class Like(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

# class Follow(models.Model):
#     pass