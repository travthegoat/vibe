from django.urls import path
from . import views

urlpatterns = [
    path('follow/<uuid:id>/', views.FollowCreateAPIView.as_view()),
    path('followers/<uuid:id>/', views.FollowersListAPIView.as_view()),
    path('followings/<uuid:id>/', views.FollowingsListAPIView.as_view()),
    path('<uuid:id>/reviews/', views.OwnedReviewListAPIView.as_view()),
]

