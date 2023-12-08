from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/', blank=True)
    background_img=models.ImageField(upload_to='bg-images/',blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user}'
    
    def users_subscribed(self):
       return Profile.objects.filter(subscriber__channel=self)
   
    def users_subscribed_cnt(self):
       return self.users_subscribed().count()
    def get_channels_subscribed(self):
        a= Subscribers.objects.filter(user=self)
        x=[]
        for b in a:
            # print((b.channel.user))
            x.append((b.channel.user.id))
        # print(x)
        return x
        
    
class Subscribers(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='subscriber')
    channel = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='channel')
    
    class Meta:
        unique_together=[
            ('channel','user'),
        ]

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/', blank=False)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    likes=models.IntegerField(default=0)
    views=models.IntegerField(default=0)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Video: {self.title} :- {self.user}"
    
    def user_has_liked(self):
        # print(User.objects.filter(videolikes__video=self))
        
        return User.objects.filter(videolikes__video=self)
    
class VideoLikes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    
    class Meta:
        unique_together=[
            ('video','user'),
        ]
        
class Comments(models.Model):
    commenter = models.ForeignKey(User,on_delete=models.CASCADE)
    video = models.ForeignKey(Video,on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(default=0)
    replies_cnt=models.IntegerField(default=0)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    
    class Meta:
        ordering=[
            '-date_posted'
        ]
    
    def __str__(self):
        return self.text[:15] + "..."
    
    def users_liked(self):
        # print('ok ',User.objects.filter(commentlikes__liked_comment=self))
        return User.objects.filter(commentlikes__liked_comment=self)

class CommentLikes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    liked_comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    
    class Meta:
        unique_together=[
            ('liked_comment','user'),
        ]

