from django.urls import path,include
from django.views.generic import TemplateView
from . import views
from .views import Signup
from .models import *
from django import forms 

urlpatterns = [
    path('', views.home , name = 'home'),
    path('Signup/',Signup.as_view(), name='signup'),
    path('Login/' ,views.user_login, name = 'login'),
    path('Dashboard/' ,views.dashboard, name = 'dashboard'),
    path('Dashboard1/' ,views.dashboard1, name = 'dashboard1'),
    path('Category/' ,views.category, name = 'category'),
    path('Book/' ,views.book, name = 'book'),
    path('Author/' ,views.author, name = 'author'),
    path('Logout/',views.logout, name = 'logout'),
    path('ContactUs',views.contact , name = "contactus"),
    path('Issuedbook',views.issue, name="issuedbook"),
]
