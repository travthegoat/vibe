from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from uuid import uuid4

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField()
    movie_id = models.TextField()
    movie_name = models.TextField()
    movie_image = models.TextField()
    movie_year = models.IntegerField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.author