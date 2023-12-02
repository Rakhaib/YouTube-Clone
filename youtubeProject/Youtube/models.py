from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/', blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user}'


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/', blank=False)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    likes=models.IntegerField(default=0)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Video: {self.title} :- {self.user}"
