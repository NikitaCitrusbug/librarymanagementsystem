from django.urls import path,include
from django.views.generic import TemplateView
from . import views
from .views import Signup ,LoginView
from .models import *
from django import forms 

urlpatterns = [
    path('', views.home),
    path('Signup/',Signup.as_view(),name='signup'),
    path('Login/' ,LoginView.as_view(), name = 'login'),
]
