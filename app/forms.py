from django import forms
from django.contrib.auth.models import User
from .models import StudyGroup


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class StudyGroupForm(forms.ModelForm):
    class Meta:
        model = StudyGroup
        fields = ['name', 'description']
