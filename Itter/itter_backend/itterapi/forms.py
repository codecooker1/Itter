from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.utils import timezone

class UserProfileForm(forms.ModelForm):
    # Fields for User Model
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, 'user'):
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email
        
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
            user.set_password(self.cleaned_data['password'])
        else:
            user = User.objects.create_user(
                username=self.cleaned_data['username'],
                email=self.cleaned_data['email'],
            )
            user.set_password(self.cleaned_data['password'])
        profile.created_at = timezone.now()
        user.save()
        profile.user = user
        profile.save()
        return profile