from rest_framework import serializers
from .models import UserProfile, Post, Like, Follow, User

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    followers = serializers.ReadOnlyField()
    following = serializers.ReadOnlyField()
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',  # Replace with your user detail view name
        read_only=True
    )

    class Meta:
        model = UserProfile
        fields = ['url', 'user', 'bio', 'profile_image', 'created_at', 'followers', 'following']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    likes = serializers.ReadOnlyField()
    user = serializers.HyperlinkedRelatedField(
        view_name='user',  # Replace with your user detail view name
        read_only=True
    )

    class Meta:
        model = Post
        fields = ['post_id', 'user', 'content', 'media_url', 'created_at', 'likes']

class LikeSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name='post-detail',  # Replace with your post detail view name
        queryset=Post.objects.all()
    )

    class Meta:
        model = Like
        fields = ['url', 'post', 'created_at']

class FollowSerializer(serializers.HyperlinkedModelSerializer):
    follower = serializers.HyperlinkedRelatedField(
        view_name='user-detail',  # Replace with your user detail view name
        queryset=User.objects.all()
    )
    followee = serializers.HyperlinkedRelatedField(
        view_name='user-detail',  # Replace with your user detail view name
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ['url', 'follower', 'followee', 'created_at']