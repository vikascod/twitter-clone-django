from django import forms
from app.models import Tweet, Profile, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['body']
        exclude = ('user', 'likes')
        widgets = {
            'body':forms.Textarea(attrs={'class':'form-control'})
        }

class ProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(label="Upload Profile Pic", widget=forms.FileInput(attrs={'class':'form-control'}))
    bio = forms.CharField(label="Bio", widget=forms.TextInput(attrs={'class':'form-control'}))
    social_link = forms.CharField(label="Social Media Link", widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Profile
        fields = ('profile_pic', 'bio', 'social_link')


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. john123'}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'e.g.user@gmail.com'}))
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. John'}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'e.g.Wick'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name', 'password1', 'password2']


class UpdateUserProfileForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. john123'}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'e.g.user@gmail.com'}))
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. John'}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'e.g.Wick'}))
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']


class CommentForm(forms.ModelForm):
    body = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Comment
        fields = ['body']
        exclude = ('user', 'tweet')