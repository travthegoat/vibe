from django.contrib import admin
from .models import CustomUser, Follows

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Follows)