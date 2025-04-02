from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReviewListCreateAPIView.as_view())
]
