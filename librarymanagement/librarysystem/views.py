import http
from re import template
from django.shortcuts import render

# Create your views here.
from urllib import request
from django.views.generic import View, CreateView
from django.shortcuts import render , redirect , reverse
from django import forms
from librarysystem import forms
from django.http import HttpResponse
from librarysystem.models import User, AbstractUser
from librarysystem.forms import CustomUserCreationForm , LoginForm
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied


def home(request):
    return HttpResponse("<h1>Welcome to The Library</h1>")

class Signup(CreateView):
    model=User
    form_class = CustomUserCreationForm
    template_name = 'user_form.html'

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg = "successfully"
            return HttpResponse(msg)
        else:
            msg = "error"
            return HttpResponse(msg)




class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', { 'form':  LoginForm })

    # really low level
    def post(self, request):
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is None:
                return render(
                    request,
                    'login.html',
                    { 'form': form, 'invalid_creds': True }
                )

            try:
                form.confirm_login_allowed(user)
            except forms.ValidationError:
                return render(
                    request,
                    'login.html',
                    { 'form': form, 'invalid_creds': True }
                )
            login(request, user)

            return redirect(reverse('login'))


# class Login(CreateView):
#     model=User
#     form_class = LoginForm
#     template_name = 'login.html'

#     def post(self,request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             msg = "login successfully"
#             return HttpResponse(msg)
#         else:
#             msg = "error"
#             return HttpResponse(msg)
