from django.urls import path,include
from django.views.generic import TemplateView
from . import views
from .views import  Home , SignupAdmin , SignupMember , Login , Dashboard , CategoryView, BookView, Issue, AuthorView , Contact
from .models import *
from django import forms 

urlpatterns = [
    path('',Home.as_view() , name = "home"),
    path('Dashboard/',Dashboard.as_view() , name = "dashboard"),
    path('Book/',BookView.as_view() , name = "book"),
    path('Category/',CategoryView.as_view() , name = "category"),
    path('Issuedbook/',Issue.as_view() , name = "issuedbook"),
    path('Author/',AuthorView.as_view() , name = "author"),
    path('ContactUs',Contact.as_view() , name = "contactus"),
    path('Adminsignup',SignupAdmin.as_view(), name = 'adminsignup'),
    path('Usersignup',SignupMember.as_view(), name = 'membersignup'),
    path('Login',Login.as_view(),name='login'),
    
    
    path('Dashboard1/' ,views.dashboard1, name = 'dashboard1'),
    path('Logout/',views.logout, name = 'logout'),
    
    
]
