# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import Post, Like, UserProfile, Follow, User

# Create a model serializer
class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = UserProfile
		fields = (('bio'), 'bio', 'profile_image', 'created_at')
