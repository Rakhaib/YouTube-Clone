from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('upload/',views.upload,name='upload'),
    path('video/<int:video_id>/',views.video_view,name='video_view'),
    path('liked_videos/',views.liked_videos,name="liked_videos"),
    path('trending/',views.trending,name="trending"),
    path('subscriptions/',views.subscriptions,name='subscriptions'),
    path('channel/<str:name>',views.channel,name='channel'),
    path('editProfile/',views.edit_profile,name='edit_profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)