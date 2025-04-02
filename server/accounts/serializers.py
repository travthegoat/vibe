from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import CustomUser, Follows

from rest_framework import serializers

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'display_name', 'profile_image', 'bio', 'joined_at']
        
class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ['id', 'username', 'email', 'display_name', 'profile_image', 'bio', 'joined_at'] 
        
class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follows
        fields = ['id', 'follower', 'following', 'followed_at']
        
class FollowerSerializer(serializers.ModelSerializer):
    follower = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = Follows
        fields = ['follower']
        
    def to_representation(self, instance):
        return CustomUserSerializer(instance.following).data
        
class FollowingSerializer(serializers.ModelSerializer):
    following = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = Follows
        fields = ['following']
        
    def to_representation(self, instance):
        return CustomUserSerializer(instance.following).data