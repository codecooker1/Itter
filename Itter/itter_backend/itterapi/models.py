from django.db import models
from django.contrib.auth.models import User
import uuid
from PIL import Image
import supabase
from django.core.exceptions import ValidationError
from urllib.parse import urlparse

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    bio = models.TextField(max_length=250)
    profile_image = models.URLField(default='https://jzydvbxwyynlezjnqbbd.supabase.co/storage/v1/object/public/profilepics/1%20(1).png')
    created_at = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return f'{self.user.username}\'s Profile'
    
    @property
    def followers(self):
        return Follow.objects.filter(followee=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(follower=self.user).count()
    
    # def change_profile_pic(self, pic):
    #     response = supabase.storage.from_('profilepics').upload('file_path', self.user.username, {'upsert': 'true'})

    def change_profile_pic(self, file_path):
        try:
            response = supabase.storage.from_('profilepics').upload(f"profilepics/{self.user.username}.png", file_path, {"upsert": True})
            if response.get("error"):
                raise ValueError(f"Upload failed:\n {response['error']}")
            self.profile_image = response.get("publicURL")
            self.save()
        except Exception as e:
            print(f"Error uploading profile picture: {e}")


    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     super().save()

    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    
def validate_media_url(value):
    parsed = urlparse(value)
    if not parsed.scheme or not parsed.netloc:
        raise ValidationError(f"{value} is not a valid URL.")

class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=250)
    media_url = models.URLField(validators=[validate_media_url], null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)
    
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
    
    def is_liked(self, user):
        return Like.objects.filter(post=self, user=user).exists() if user.is_authenticated else False

# class Repost(models.Model):
#     pass

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'post')

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    followee = models.ForeignKey(User, related_name='followee', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('follower', 'followee')

    def clean(self):
        if self.follower == self.followee:
            raise ValidationError("Users cannot follow themselves.")
        
    def __str__(self):
        return f"{self.follower.username} follows {self.followee.username}"
