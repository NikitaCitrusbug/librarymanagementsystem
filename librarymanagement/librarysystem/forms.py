from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name','email']

    def save(self,commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user



class LoginForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username' , 'password']




