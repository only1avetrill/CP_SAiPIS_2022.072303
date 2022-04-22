import requests
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, AddAdForm
from .models import Ad

def AboutPage(request):
    return render(request, 'about.html')

def AuthPage(request):
    return render(request, 'auth_page.html')

def MainPage(request):
    ads = Ad.objects.all()
    return render(request, 'main.html', {'ads': ads})

def sort(request, sort_slug):
    ads = Ad.objects.order_by(sort_slug)
    return render(request, 'main.html', {'ads': ads})


def ExecutorsPage(request):
    return render(request, 'executors.html')

def ProfilePage(request):
    return render(request, 'profile.html')

def AddAdsPage(request):
    if request.method == 'POST':
        form = AddAdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    form = AddAdForm()
    data = {
        'form': form,
    }

    return render(request, 'add_ad.html', data)

def RegisterUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth')

    form = CreateUserForm
    context = {'form': form}
    return render(request, 'register.html', context)

