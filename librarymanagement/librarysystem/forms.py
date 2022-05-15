from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Author, Category, User , Book

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name','email']

    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_librarian = True
        if commit:
            user.save()
        return user

class CustomMemberCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name','email']

    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_member = True
        if commit:
            user.save()
        return user



class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'password']



class AddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'



