from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import CustomUser

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'display_name', 'profile_image', 'bio', 'joined_at']
        
class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ['id', 'username', 'email', 'display_name', 'profile_image', 'bio', 'joined_at'] 