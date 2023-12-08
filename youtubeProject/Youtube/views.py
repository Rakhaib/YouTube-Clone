from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, VideoUploadForm, CommentForm, ProfileEditForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile, Video, VideoLikes, Comments, CommentLikes, Subscribers


# Create your views here.

def home(request):
    user = request.user
    all_videos = Video.objects.all().order_by('-upload_date')
    return render(request, 'home.html', {'user': user, 'videos': all_videos})


def register(request):
    if (request.user.is_authenticated):
        return redirect('home')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if (request.user.is_authenticated):
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

@login_required
def edit_profile(request):
    print('ok')
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('channel',name=request.user.username)  # Redirect to the user's profile page
    else:
        form = ProfileEditForm(instance=request.user.profile)
    
    return render(request, 'edit_profile.html', {'form': form})


@login_required(login_url='/login/')
def upload(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('home')
    else:
        form = VideoUploadForm()

    return render(request, 'upload_video.html', {'form': form})

@login_required(login_url='/login/')
def liked_videos(request):
    liked=VideoLikes.objects.filter(user=request.user)
    liked_videos=[]
    for video in liked:
        liked_videos.append(video.video)
    context={
        'liked_videos':liked_videos,
    }
    return render(request,'liked_videos.html',context)
@login_required(login_url='/login/')
def subscriptions(request):
    
    # print(request.user.profile)
    current_profile=(request.user.profile)
    # print('ok')
    channel_id=current_profile.get_channels_subscribed()
    # print(channel_id)
    # print(Profile.objects.filter(channel__subscriber=request.user.profile))
    uploaded_videos = Video.objects.filter(user_id__in=channel_id)
    # print(uploaded_videos)
    context={
        'videos':uploaded_videos
    }
    return render(request,'subscriptions.html',context)

def trending(request):
    trending_videos=Video.objects.all().order_by('-views')
    context={
        'videos':trending_videos
    }
    return render(request,'trending.html',context)

def channel(request,name):
    channel=User.objects.get(username=name)
    channel_videos=Video.objects.filter(user=channel)
    
    if request.method == "POST":
        input_type = request.POST.get('video_id')
        if (input_type== 'subscribe'):
                print('ok')
                subscribe_to = int(request.POST.get('subscribe'))
                # print(subscribe_to)
                user=channel
                # print(user)
                profile=Profile.objects.get(user=user)
                subscribed_users=(profile.users_subscribed())
                print(subscribed_users)
                if(request.user.profile in subscribed_users):
                    print('present')
                    Subscribers.objects.filter(user=request.user.profile,channel=profile).delete()
                    print('deleted')
                else:
                    print('not-present')
                    Subscribers.objects.create(user=request.user.profile,channel=profile)
                    print('created')
    context={
        'videos':channel_videos,
        'channel':channel,
    }
    return render(request,'channel_view.html',context)

def video_view(request, video_id):

    video = get_object_or_404(Video, pk=video_id)
    all_comments = Comments.objects.filter(video=video)
    video.views += 1
    video.save()
    comment_form = CommentForm(request.POST)

    videos = Video.objects.all()

    if request.user.is_authenticated:
        liked_video = VideoLikes.objects.filter(
            user=request.user, video=video_id).exists()

    if request.method == "POST" :
        if not request.user.is_authenticated:
            return redirect('login')
        input_type = request.POST.get('video_id')

        if (input_type == 'like' and not liked_video):
            print('liked')
            VideoLikes.objects.create(user=request.user, video=video)
            video.likes += 1
            video.views -= 2
            video.save()
            return redirect('video_view', video_id=video_id)

        if (input_type == 'like' and liked_video):
            print('unliked')
            video.likes -= 1
            video.views -= 2
            VideoLikes.objects.filter(user=request.user, video=video).delete()
            video.save()
            return redirect('video_view', video_id=video_id)

        if (input_type == 'new_comment'):
            if comment_form.is_valid():
                new_comment = Comments(
                    text=request.POST['text'], commenter=request.user, video=video)
                new_comment.save()
                video.views -= 1
                return redirect('video_view', video_id=video_id)

        if (input_type in ['com_like', 'com_dislike']):
            comment_id = int(request.POST.get('comment_id'))
            com = get_object_or_404(Comments, pk=comment_id)
            like_obj = CommentLikes.objects.filter(
                liked_comment=com, user=request.user).exists()
            if input_type == 'com_like':
                if like_obj:
                    com.likes -= 1
                    com.save()
                    CommentLikes.objects.filter(
                        liked_comment=com, user=request.user).delete()
                else:
                    com.likes += 1
                    com.save()
                    CommentLikes.objects.create(
                        liked_comment=com, user=request.user)
            else:
                if like_obj:
                    com.likes -= 1
                    com.save()
                    CommentLikes.objects.filter(
                        liked_comment=com, user=request.user).delete()
            return redirect('video_view', video_id=video_id)

        if (input_type == 'sub_comment'):
            if comment_form.is_valid():

                comment_id = int(request.POST.get('parent-com-id'))
                parent_comment = get_object_or_404(Comments, pk=comment_id)
                parent_comment.replies_cnt += 1
                parent_comment.save()
                Comments.objects.create(
                    text=request.POST['text'], commenter=request.user, video=video, parent_comment=parent_comment)
                return redirect('video_view', video_id=video_id)
        
        if (input_type== 'subscribe'):
            print('ok')
            subscribe_to = int(request.POST.get('subscribe'))
            # print(subscribe_to)
            user=User.objects.get(pk=subscribe_to)
            # print(user)
            profile=Profile.objects.get(user=user)
            subscribed_users=(profile.users_subscribed())
            print(subscribed_users)
            if(request.user.profile in subscribed_users):
                print('present')
                Subscribers.objects.filter(user=request.user.profile,channel=profile).delete()
                print('deleted')
            else:
                print('not-present')
                Subscribers.objects.create(user=request.user.profile,channel=profile)
                print('created')
            
        
    context = {
        'cur_video': video,
        'videos': videos,
        'comments': all_comments,
        'com_count': all_comments.count(),
        'com_form': comment_form,
        'current_url': request.build_absolute_uri(),
    }

    return render(request, 'video.html', context)
