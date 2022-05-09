from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import Signup
from .models import *
from django import forms 

urlpatterns = [
    path('signup/',Signup.as_view(),name='signup'),
]
