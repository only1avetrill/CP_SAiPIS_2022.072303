from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthPage, name='auth'),
    path('ad/sort/<slug:sort_slug>', views.sort, name='sort'),
    path('about', views.AboutPage, name='about'),
    path('main', views.MainPage, name='main'),
    path('register', views.RegisterUser, name='register'),
    path('executors', views.ExecutorsPage, name='executors'),
    path('profile', views.ProfilePage, name='profile'),
    path('add_ad', views.AddAdsPage, name='addad'),
]
