from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions

from .models import Review
from .serializers import *

import random

class ReviewListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        queryset = list(Review.objects.all())
        random.shuffle(queryset)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)