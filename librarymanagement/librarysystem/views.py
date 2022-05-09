from django.shortcuts import render

# Create your views here.
from urllib import request
from django.views.generic import View, CreateView
from django.shortcuts import render
from django import forms
from librarysystem import forms
from django.http import HttpResponse
from librarysystem.models import User, AbstractUser
from librarysystem.forms import CustomUserCreationForm


class Signup(CreateView):
    model=User
    form_class = CustomUserCreationForm
    template_name = 'user_form.html'

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg = "success"
            return HttpResponse(msg)
        else:
            msg = "error"
            return HttpResponse(msg)
