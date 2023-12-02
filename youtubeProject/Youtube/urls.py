from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('upload/',views.upload,name='upload')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)