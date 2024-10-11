from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'password', 'username', 'bio']

    def save(self, commit=True) -> UserProfile:
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
