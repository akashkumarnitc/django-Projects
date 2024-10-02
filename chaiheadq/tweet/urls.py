# tweet/urls.py
from django.urls import path
from tweet import views
urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),  # List of tweets
    path('create/', views.tweet_create, name='tweet_create'),  # Create a new tweet
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),  # Edit a tweet
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),  # Delete a tweet
    path('register/', views.register, name='register'),  # User registration
]