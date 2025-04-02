from rest_framework import serializers

from .models import Review
from accounts.serializers import CustomUserSerializer

class ReviewSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'author', 'caption', 'movie_id', 'movie_name', 'movie_image', 'movie_year', 'rating', 'created_at' ]
        
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'author', 'caption', 'movie_id', 'movie_name', 'movie_image', 'movie_year', 'rating', 'created_at' ]