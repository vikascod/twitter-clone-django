from django.urls import path
from app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('user-profile/', views.user_profile, name='profile_list'),
    path('update-user-profile/', views.update_user_profile, name='user_profile'),
    path('profile/<int:pk>/', views.profile_view, name='profile'),
    path('tweet-like/<int:pk>/', views.tweet_like, name='tweet_like'),
    path('tweet-comment/<int:pk>/', views.comment_view, name='comment'),
    path('comment-delete/<int:pk>/', views.comment_delete, name='comment_delete'),
    path('comment-edit/<int:pk>/', views.comment_update_view, name='comment_update'),
    path('unfollow/<int:pk>/', views.unfollow, name='unfollow'),
    path('follow/<int:pk>/', views.follow_view, name='follow'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/followers/<int:pk>/', views.follower_list, name='follower_list'),
    path('profile/following/<int:pk>/', views.following_list, name='following_list'),
    path('delete-tweet/<int:pk>/', views.delete_tweet, name='delete_tweet'),
    path('edit-tweet/<int:pk>/', views.update_tweet, name='update_tweet'),
]