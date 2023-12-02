from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ['user','upload_date','video_file']
    
@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['user']
