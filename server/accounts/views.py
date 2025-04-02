from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser

from .serializers import *

class FollowCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, id):
        data = {
            "follower": request.user.id,
            "following": id
        }
        
        serializer = FollowSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
    
class FollowersListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, id):
        try:
            user = CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            return Response({ "message": "User does not exists!" })
        
        followers = Follows.objects.filter(following=id)
        serializer = FollowerSerializer(followers, many=True)
        return Response({ "follower_count": followers.count(), "followers": serializer.data})
        
class FollowingsListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, id):
        try:
            user = CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            return Response({ "message": "User does not exists!" })
        
        followings = Follows.objects.filter(follower=id)
        serializer = FollowingSerializer(followings, many=True)
        return Response({ "following_count": followings.count(), "followings": serializer.data})