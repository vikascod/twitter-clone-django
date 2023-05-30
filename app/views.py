from django.shortcuts import render, redirect, get_object_or_404
from app.models import Profile, Tweet
from django.contrib import messages
from app.forms import TweetForm, SignUpForm, UpdateUserProfileForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def home(request):
    if request.user.is_authenticated:
        form = TweetForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                messages.success(request, "Successfully posted")
                return redirect('home')
        tweets = Tweet.objects.all().order_by('-created_on')
        return render(request, 'app/home.html', {'tweets':tweets, 'form':form})
    else:
        tweets = Tweet.objects.all().order_by('-created_on')
        return render(request, 'app/home.html', {'tweets':tweets})


def user_profile(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        context = {
            'profiles':profiles
        }
        return render(request, 'app/profile_list.html', context)
    else:
        messages.warning(request, "You must be logged in")
        return redirect('home')


def profile_view(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(id=pk)
        tweets = Tweet.objects.filter(user=pk)
        if request.method == "POST":
            current_user = request.user.profile
            action = request.POST['follow']
            if action == "unfollow":
                current_user.follows.remove(profile)
            elif action == "follow":
                current_user.follows.add(profile)
            current_user.save()
        return render(request, 'app/profile.html', {"profile":profile, 'tweets':tweets})
    else:
        messages.warning(request, "You must be logged in")
        return redirect('home')


@login_required(login_url='login')
def unfollow(request, pk):
    profile = Profile.objects.get(user_id=pk)
    request.user.profile.follows.remove(profile)
    request.user.profile.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def follow_view(request, pk):
    user_profile = Profile.objects.get(user_id=pk)
    request.user.profile.follows.add(user_profile)
    request.user.profile.save()
    return redirect(request.META.get('HTTP_REFERER'))


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "successfully Logged in")
                return redirect('home')
            else:
                messages.warning(request, "Invalid Username or Password")
                return redirect('login')
        return render(request, 'app/login.html')
    else:
        messages.warning(request, 'You have already logged In!!')
        return redirect('home')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        messages.warning(request, "You haven't logged in yet!!")
        return redirect('login')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                if User.objects.filter(username=username).exists():
                    messages.warning(request, "Username already exists.")
                    return redirect('signup')
                elif User.objects.filter(email=email).exists():
                    messages.warning(request, "Email already exists.")
                    return redirect('signup')
                else:
                    form.save()
                    messages.success(request, "Account created!")
                    return redirect('login')
            else:
                messages.warning(request, "Something went wrong!")
                return redirect('signup')
        form = SignUpForm()
        return render(request, 'app/signup.html', {'form':form})
    else:
        messages.warning(request, 'You have already logged in!')
        return redirect('home')


@login_required(login_url='login')
def update_user_profile(request):
    current_user = User.objects.get(id=request.user.id)
    profile_user = Profile.objects.get(user__id=request.user.id)
    user_form = UpdateUserProfileForm(request.POST or None, request.FILES or None, instance=current_user)
    profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=profile_user)
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        login(request, current_user)
        messages.success(request, "Successfully Profile updated!!")
        return redirect('profile', pk=current_user.id)
    return render(request, 'app/update_user_profile.html', {'user_form':user_form, 'profile_form':profile_form})


@login_required(login_url='login')
def tweet_like(request, pk):
    tweet = get_object_or_404(Tweet, id=pk)
    liked = tweet.likes.filter(id=request.user.id)
    if liked:
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def tweet_shere(request, pk):
    tweet = get_object_or_404(Tweet, id=pk)
    if tweet:
        return render(request, 'app/tweet_share.html', {'tweet':tweet})
    else:
        messages.warning(request, "Tweet doesn't not exists!")
        return redirect(request.META.get('HTTP_REFERER'))

