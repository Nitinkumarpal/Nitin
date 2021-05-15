from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from django.conf import settings
from .views import *
from  . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('base/',views.base, name='base'),
    path('login/',views.login_request, name='login'),
     path("logout/", views.Slogout, name="logout"),


    path('signup/',views.signup, name='signup'),
    path('editsignup/',views.editsignup, name='editsignup'),
    path('contact/',views.Contact, name='contact'),
    path('createblog/',views.create_blog, name='createblog'),
    path('blogsdetails/',views.blogs_details, name='blogsdetails'),
    url(r'^password/$', views.change_password, name='change_password'),

    path('<slug:slug>/', views.blogs.as_view(), name='post_detail'),

]