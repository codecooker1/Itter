from django.db import models
from django.contrib.auth.models import User
import uuid
from PIL import Image

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    bio = models.TextField(max_length=250)
    profile_image = models.ImageField(default='default.png', upload_to='profile_pics')
    created_at = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return f'{self.user.username}\'s Profile'
    
    @property
    def followers(self):
        return Follow.objects.filter(follower=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(followee=self.user).count()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=250)
    media_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (
            f"{self.user} "
            f"with id {self.post_id}"
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.content[:30]}..."
        )
        
    @property
    def likes(self): 
        return Like.objects.filter(post=self).count()

# class Repost(models.Model):
#     pass

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    followee = models.ForeignKey(User, related_name='followee', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)