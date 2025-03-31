from django.db import models
from django.contrib.auth.models import AbstractUser

from uuid import uuid4

# Create your models here.
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    display_name = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username