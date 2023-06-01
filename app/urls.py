from django.urls import path
from app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('user-profile/', views.user_profile, name='profile_list'),
    path('update-user-profile/', views.update_user_profile, name='user_profile'),
    path('profile/<int:pk>/', views.profile_view, name='profile'),
    path('tweet-like/<int:pk>/', views.tweet_like, name='tweet_like'),
    path('tweet-comment/<int:pk>/', views.comment_view, name='comment'),
    path('unfollow/<int:pk>/', views.unfollow, name='unfollow'),
    path('follow/<int:pk>/', views.follow_view, name='follow'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]