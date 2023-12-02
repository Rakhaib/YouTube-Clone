from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm, VideoUploadForm
from django.http import HttpResponse
from .models import Video


# Create your views here.

def home(request):
    user=request.user
    all_videos=Video.objects.all()
    return render(request,'home.html',{'user':user,'videos':all_videos})

def video_player(request):
    return render (request,'video_player.html',{'url':'video_url'})

def register(request):
    if(request.user.is_authenticated):
        return redirect('home')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home') 
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
def login_view(request):
    if(request.user.is_authenticated):
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')   
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home') 

@login_required(login_url='/login/')
def upload(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user  # Assuming you have user authentication in place
            video.save()
            return redirect('home')  # Redirect to a success page or wherever you want
    else:
        form = VideoUploadForm()

    return render(request, 'upload_video.html', {'form': form})