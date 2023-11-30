from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.http import HttpResponse


# Create your views here.

def home(request):
    user=request.user
    return render(request,'home.html',{'user':user})

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
    return HttpResponse(f"OK, {request.user.username}")