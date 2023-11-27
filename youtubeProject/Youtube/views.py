from django.shortcuts import render

# Create your views here.

def video_player(request):
    return render (request,'video_player.html',{'url':'video_url'})
