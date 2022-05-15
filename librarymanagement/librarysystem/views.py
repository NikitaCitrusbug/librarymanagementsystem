import http
from multiprocessing import context
from re import template
from django.shortcuts import render

# Create your views here.
from urllib import request
from django.views.generic import View, CreateView , TemplateView
from django.shortcuts import render , redirect , reverse
from django import forms
from librarysystem import forms
from django.http import HttpResponse, HttpResponseRedirect
from librarysystem.models import Author, Category, User, AbstractUser , Book
from librarysystem.forms import AddForm, CustomUserCreationForm , LoginForm , AddCategoryForm , AddAuthorForm , CustomMemberCreationForm
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView 




class Home(View):
    template_name = 'home.html'
    def get(self,request):
        return render(request,self.template_name)


class Dashboard(View):
    template_name = 'dashboard.html'
    def get(self,request):
        return render(request,self.template_name)



class BookView(View):
    template_name = 'book/book.html'
    def get(self,request):
        return render(request,self.template_name)

class AddBook(CreateView):
    model=Book
    form_class = AddForm
    template_name = 'book/add_book.html'

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('error')

class BookRetrieve(ListView):
    model = Book
    template_name = 'book/book_list.html'

class BookDetail(DetailView):  
    model = Book

class BookUpdate(UpdateView):  
    model = Book

class CategoryView(View):
    template_name = 'category/Category.html'
    def get(self,request):
        return render(request,self.template_name)

class AddCategory(CreateView):
    model=Category
    form_class = AddCategoryForm
    template_name = 'category/add_category.html'

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('add category')
        else:
            return HttpResponse('error')

class CategoryRetrieve(ListView):
    model = Category

class CategoryDetail(DetailView):  
    model = Category

class CategoryUpdate(UpdateView):  
    model = Category 

class AuthorView(View):
    template_name = 'author/author.html'
    def get(self,request):
        return render(request,self.template_name)

class AddAuthor(CreateView):
    model= Author
    form_class = AddAuthorForm
    template_name = 'author/add_author.html'

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('add author')
        else:
            return HttpResponse('error')

class AuthorRetrieve(ListView):
    model = Author

class AuthorDetail(DetailView):  
    model = Author

class AuthorUpdate(UpdateView):  
    model = Author



class Issue(View):
    template_name = 'issue.html'
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
            
            return HttpResponseRedirect('/Dashboard1/')
        else:
            
            return HttpResponseRedirect('/')


class SignupMember(CreateView):
    model=User
    form_class = CustomMemberCreationForm
    template_name = 'signup_member.html'

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Dashboard/')
        else:
            return HttpResponseRedirect('/')


class Login(View):
#     model=User
#     form_class = LoginForm
#     def get(self,request):
#         form = self.form_class
#         return render(request,'login.html',{'form' : form})


#     def post(self,request):
#         username=request.POST['username']
#         password=request.POST['password']
#         print(password)
#         pwd=User.objects.get(username=username)
#         print(username)
#         password=pwd.password
#         print(password)
#         valid = check_password(password,password)
#         print(valid)
        
#         if not valid:
#             return  HttpResponse("incorrect password")
            

#         user=User.objects.get(username=username) 
#         if user.is_authenticated:

#             if user.is_librarian == True:
#                 login(request, user)
#                 return render(request,'dashboard1.html')
#             else:
#                 login(request,user)
#                 return render(request,'dashboard.html') 
#         else:
#             return HttpResponse("invalid login")




    model=User
    form_class = LoginForm
    template_name = 'login.html'
    def get(self,request):
        form=self.form_class(request.POST)
        return render(request,self.template_name,{'form' : form})


    def post(self,request):
        username = request.POST['username']
        passw =request.POST['password']
        # print(username,passw)
        pwd = User.objects.get(username=username)
        # a = User.objects.all()
        print('data',pwd)
        password=pwd.password
        valid = check_password(passw,password)
        
        if not valid:
            return  HttpResponse("incorrect password")

        user=User.objects.get(username=username)
        if user.is_authenticated:

            if user.is_librarian == True:
                login(request, user)
                return  HttpResponseRedirect('/Dashboard1/')
            else:
                login(request,user)
                return  HttpResponseRedirect('/Dashboard/')
        else:
            msg = "invalid login"
            return HttpResponse(msg)