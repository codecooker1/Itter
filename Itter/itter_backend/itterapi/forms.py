from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Post
from django.utils import timezone

class UserProfileForm(forms.ModelForm):
    # Fields for User Model
    username = forms.CharField()
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, 'user'):
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email
            self.fields['firstname'].initial = self.instance.user.first_name
            self.fields['lastname'].initial = self.instance.user.last_name
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if self.instance and hasattr(self.instance, 'user'):
            if User.objects.filter(email=email).exclude(pk=self.instance.user.pk).exists():
                raise forms.ValidationError("This email is already in use.")
        elif User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
    
    def save(self):
        profile = super().save(commit=False)
        
        if  hasattr(profile, 'user'):
            user = self.instance.user
            user.username = self.cleaned_data['username']
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['firstname']
            user.last_name = self.cleaned_data['lastname']
        else:
            user = User.objects.create_user(
                username=self.cleaned_data['username'],
                email=self.cleaned_data['email'],
                first_name=self.cleaned_data['firstname'],
                last_name=self.cleaned_data['lastname'],
            )
        
        user.set_password(self.cleaned_data['password'])
        profile.created_at = timezone.now()
        user.save()
        profile.user = user
        profile.save()
        return profile

class PostForm(forms.ModelForm):
    media_url = forms.URLField(required=False)
    class Meta:
        model = Post
        fields = ('content',)
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, 'media_url'):
            self.fields['media_url'].initial = self.instance.media_url
            
    def save(self):
        post = super().save(commit=False)
        post.created_at = timezone.now()
        post.user = self.user
        if hasattr(post, 'media_url'):
            post.media_url = self.cleaned_data['media_url']
        else:
            post.media_url = '#'
        post.save()
        return post
