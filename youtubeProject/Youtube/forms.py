# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Video, Comments, Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title','description','video_file','thumbnail']
        widgets = {
            'video_file': forms.FileInput(attrs={'accept': 'video/mp4'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder':'Add a comment...'}),
        }
        
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=[
            'background_img','image','bio'
        ]