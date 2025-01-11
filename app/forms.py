from django import forms
from django.contrib.auth.models import User
from .models import StudyGroup
from .models import Profile
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    # confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
    
    # def clean_confirm_password(self):
    #     password = self.cleaned_data.get("password")
    #     confirm_password = self.cleaned_data.get("confirm_password")
        
    #     if password != confirm_password:
    #         raise ValidationError("Passwords do not match")
    #     return confirm_password


class StudyGroupForm(forms.ModelForm):
    class Meta:
        model = StudyGroup
        fields = ['name', 'description']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

class BioForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']