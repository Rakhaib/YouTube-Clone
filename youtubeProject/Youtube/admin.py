from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ['user','upload_date','video_file']
    
@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['user']

admin.site.register(models.VideoLikes)

admin.site.register(models.Subscribers)

admin.site.register(models.Comments)
admin.site.register(models.CommentLikes)