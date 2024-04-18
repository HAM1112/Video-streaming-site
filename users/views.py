from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from videos.forms import VideoForm
from videos.models import Video


# Home page
def index(request):

    if request.method == 'POST':
        form = VideoForm(request.POST , request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            video = form.cleaned_data['video_file']
            video = Video.objects.create(name=name , video_file= video , user= request.user)
            video.save()
            return redirect('home')
        else:
            videos = Video.objects.all()
            return render(request, 'index.html', {'form': form , "error" : 'upload video file only' , 'videos' : videos})

    
    form = VideoForm()
    videos = Video.objects.all()
    return render(request, 'index.html' , {'form': form , 'videos' : videos})

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')