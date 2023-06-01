from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name='followed_by', symmetrical=False, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/')
    bio = models.TextField(null=True, blank=True)
    social_link = models.CharField(max_length=200, null=True, blank=True)
    updated_date = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return self.user.username
    


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

        #User can follow itself to see their posts
        # user_profile.follows.set([instance.profile.id])
        # user_profile.save()

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='tweet_like', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.user} : {self.body}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.body}"