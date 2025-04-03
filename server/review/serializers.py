from rest_framework import serializers

from .models import Review
from accounts.serializers import CustomUserSerializer

class ReviewSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'author', 'caption', 'movie_id', 'movie_name', 'movie_image', 'movie_year', 'rating', 'created_at' ]  
        
    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        
        request = self.context.get('request')
        if request and request.method in ['PATCH', 'PUT']:
            for field in ['caption', 'movie_id', 'movie_name', 'movie_image', 'movie_year', 'rating']:
                self.fields[field].required = False