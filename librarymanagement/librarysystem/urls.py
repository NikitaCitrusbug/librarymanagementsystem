from django.urls import path,include
from django.views.generic import TemplateView
from . import views
from .views import  AddAuthor, BookRetrieve, Home , SignupAdmin , SignupMember , Login , Dashboard , CategoryView, BookView, Issue, AuthorView , Contact,AddBook , AddCategory , AddAuthor , AuthorRetrieve , CategoryRetrieve
from .models import *
from django import forms 

urlpatterns = [
    path('',Home.as_view() , name = "home"),
    
    path('Adminsignup',SignupAdmin.as_view(), name = 'adminsignup'),
    path('Usersignup',SignupMember.as_view(), name = 'membersignup'),
    path('Login',Login.as_view(),name='login'),
    path('Dashboard/',Dashboard.as_view() , name = "dashboard"),
    
    path('Issuedbook/',Issue.as_view() , name = "issuedbook"),
    path('Author/',AuthorView.as_view() , name = "author"),
    path('ContactUs',Contact.as_view() , name = "contactus"),
    path('Book/',BookView.as_view() , name = "book"),
    path('Category/',CategoryView.as_view() , name = "category"),

    path('Addbook/',AddBook.as_view() , name = "addbook"),
    path('Addcategory/',AddCategory.as_view() , name = "addcategory"),
    path('Addauthor/',AddAuthor.as_view() , name = "addauthor"),

    path('retrieve/',BookRetrieve.as_view() , name = "bookretrieve"),
    path('retrieve/',AuthorRetrieve.as_view() , name = "authorretrieve"),
    path('retrieve/',CategoryRetrieve.as_view() , name = "categoryretrieve"),

    path('retrieve/<int:pk>', views.BookDetail.as_view(), name = 'bookdetail'),
    path('retrieve/<int:pk>', views.AuthorDetail.as_view(), name = 'authordetail'),
    path('retrieve/<int:pk>', views.CategoryDetail.as_view(), name = 'categorydetail'),

    path('<int:pk>/update/', views.BookUpdate.as_view(), name = 'bookupdate'),
    path('<int:pk>/update/', views.AuthorUpdate.as_view(), name = 'authorupdate'),
    path('<int:pk>/update/', views.CategoryUpdate.as_view(), name = 'categoryupdate'),
 

    
    
    path('Dashboard1/' ,views.dashboard1, name = 'dashboard1'),
    path('Logout/',views.logout, name = 'logout'),
    
    
]
