import requests
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, request
from django.urls import reverse_lazy

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

from .forms import CreateUserForm, AddAdForm, AddExecutorForm
from .models import Ad, Executor


@login_required
def AboutPage(request):
    return render(request, 'about.html')


@login_required
def MainPage(request):
    ads = Ad.objects.all()
    return render(request, 'main.html', {'ads': ads})


@login_required
def sortAds(request, sort_slug):
    ads = Ad.objects.order_by(sort_slug)
    return render(request, 'main.html', {'ads': ads})


@login_required
def sortExecutors(request, sort_slug):
    executors = Executor.objects.order_by(sort_slug)
    return render(request, 'executors.html', {'executors': executors})


@login_required
def AddSuccess(request):
    return render(request, 'add_success.html')


@login_required
def ExecutorsPage(request):
    executors = Executor.objects.all()
    return render(request, 'executors.html', {'executors': executors})


@login_required
def AnalyticsPage(request):
    user_count = User.objects.all().count()
    executor_count = Executor.objects.all().count()
    ad_count = Ad.objects.all().count()

    data = {
        'user_count': user_count,
        'executor_count': executor_count,
        'ad_count': ad_count
    }

    return render(request, 'analytics.html', data)


@login_required
def AddAdsError(request):
    return render(request, 'add_ad_error.html')


@login_required
def AddExecutorsError(request):
    return render(request, 'add_executor_error.html')


@login_required
def AddAdsPage(request):
    if request.method == 'POST':
        form = AddAdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addsuccess')
        else:
            return redirect('aderror')
        super(Event, self).save(*args, **kwargs)

    form = AddAdForm()
    data = {
        'form': form,
    }
    return render(request, 'add_ad.html', data)


@login_required
def AddExecutorsPage(request):
    if request.method == 'POST':
        form = AddExecutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addsuccess')
        else:
            return redirect('execerror')
        super(Event, self).save(*args, **kwargs)

    form = AddExecutorForm()
    data = {
        'form': form,
    }
    return render(request, 'add_executor.html', data)


def RegisterUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth')

    form = CreateUserForm
    context = {'form': form}
    return render(request, 'register.html', context)


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'auth_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('main')


@login_required
def logout_user(request):
    logout(request)
    return redirect('auth')


def LoginRequired(request):
    return render(request, 'login_required.html')


@login_required
def DeleteExecutor(request, id):
    executor = Executor.objects.get(id=id)
    executor.delete()
    return redirect('executors')


@login_required
def DeleteAd(request, id):
    ads = Ad.objects.get(id=id)
    ads.delete()
    return redirect('main')


@login_required
def EditExecutor(request, id):
    executor = Executor.objects.get(id=id)
    form = AddExecutorForm(instance=executor)

    if request.method == 'POST':
        form = AddExecutorForm(request.POST, instance=executor)
        if form.is_valid():
            form.save()
            return redirect('addsuccess')
        else:
            return redirect('execerror')
        super(Event, self).save(*args, **kwargs)

    data = {
        'form': form,
    }

    return render(request, 'edit_executor.html', data)

@login_required
def EditAd(request, id):
    ad = Ad.objects.get(id=id)
    form = AddAdForm(instance=ad)

    if request.method == 'POST':
        form = AddAdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('addsuccess')
        else:
            return redirect('aderror')
        super(Event, self).save(*args, **kwargs)

    data = {
        'form': form,
    }

    return render(request, 'edit_ad.html', data)


