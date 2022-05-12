import http
from re import template
from django.shortcuts import render

# Create your views here.
from urllib import request
from django.views.generic import View, CreateView 
from django.shortcuts import render , redirect , reverse
from django import forms
from librarysystem import forms
from django.http import HttpResponse, HttpResponseRedirect
from librarysystem.models import User, AbstractUser
from librarysystem.forms import CustomUserCreationForm , LoginForm
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password



class Home(View):
    template_name = 'home.html'
    def get(self,request):
        return render(request,self.template_name)


class Dashboard(View):
    template_name = 'dashboard.html'
    def get(self,request):
        return render(request,self.template_name)

class CategoryView(View):
    template_name = 'Category.html'
    def get(self,request):
        return render(request,self.template_name)

class BookView(View):
    template_name = 'book.html'
    def get(self,request):
        return render(request,self.template_name)

class Issue(View):
    template_name = 'issue.html'
    def get(self,request):
        return render(request,self.template_name)

class AuthorView(View):
    template_name = 'author.html'
    def get(self,request):
        return render(request,self.template_name)

class Contact(View):
    template_name = 'contact.html'
    def get(self,request):
        return render(request,self.template_name)


def logout(request):
    return HttpResponseRedirect('/')

def dashboard1(request):
    return render(request, 'dashboard1.html')



class SignupAdmin(CreateView):
    model=User
    form_class = CustomUserCreationForm
    template_name = 'signup_admin.html'

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg = "successfully"
            return HttpResponse(msg)
        else:
            msg = "error"
            return HttpResponse(msg)


class SignupMember(CreateView):
    model=User
    form_class = CustomUserCreationForm
    template_name = 'signup_member.html'

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg = "successfully"
            return HttpResponse(msg)
        else:
            msg = "error"
            return HttpResponse(msg)


class Login(View):
    model=User
    form_class = LoginForm
    template_name = 'login.html'
    def get(self,request):
        form=self.form_class(request.POST)
        return render(request,self.template_name,{'form' : form})


    def post(self,request):
        username = request.POST['username']
        password=request.POST['password']
        pwd=User.objects.get(username=username)
        password=pwd.password
        valid = check_password(password,password)
        
            

        user=User.objects.get(username=username)
        if user.is_authenticated:

            if user.is_librarian == True:
                login(request, user)
                return  HttpResponse("admin login")
            else:
                login(request,user)
                return  HttpResponse("member login")
        else:
            return HttpResponse("invalid login")