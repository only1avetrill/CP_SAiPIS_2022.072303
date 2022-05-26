import requests
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, request
from django.urls import reverse_lazy
import datetime
from datetime import timedelta
from django.views.generic.detail import DetailView

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.db.models import Q
from online_users.models import OnlineUserActivity

from .forms import *
from .models import Ad, Executor, MethodMarks, MonkeyIsVoted

Monkey = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


@login_required
def AboutPage(request):
    return render(request, 'about.html')


@login_required
def MainPage(request):
    timeToday = datetime.date.today()

    ads = Ad.objects.all()

    search = request.GET.get('search', '')
    if search:
        ads = Ad.objects.filter(
            Q(title__icontains=search) | Q(budget__icontains=search) | Q(address_city__icontains=search))
    else:
        Ad.objects.all()

    data = {
        'timeToday': timeToday,
        'ads': ads,
    }

    return render(request, 'main.html', data)


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

    search = request.GET.get('search', '')
    if search:
        executors = Executor.objects.filter(Q(title__icontains=search) | Q(price__icontains=search))
    else:
        Executor.objects.all()

    return render(request, 'executors.html', {'executors': executors})


@login_required
def AnalyticsPage(request):
    labels = []
    data = []
    queryset = Executor.objects.all()
    for executor in queryset:
        labels.append(executor.title)
        data.append(executor.price)

    user_count = User.objects.all().count()
    executor_count = Executor.objects.all().count()
    ad_count = Ad.objects.all().count()

    user_activity_objects = OnlineUserActivity.get_user_activities((timedelta(minutes=1)))
    number_of_active_users = user_activity_objects.count()

    data = {
        'user_count': user_count,
        'executor_count': executor_count,
        'ad_count': ad_count,
        'online': number_of_active_users,
        'labels': labels,
        'data': data
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
            uname = request.POST.get('username')
            type_ = request.POST.get('type')
            form.email = type_
            form.save()
            us = User.objects.get(username=uname)
            us.first_name = type_
            us.save()
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


def ExpertRank(request):
    # expert1 = 0,14
    # expert2 = 0,69
    # expert3 = 0,17

    executors = Executor.objects.all().order_by('-id')[:3]
    isVoted = MonkeyIsVoted.objects.all()

    if request.method == "POST":
        mark1 = request.POST['mark1']
        mark2 = request.POST['mark2']
        mark3 = request.POST['mark3']
        marks = MethodMarks.objects.create(mark1=mark1, mark2=mark2, mark3=mark3)
        marks.save()
        user = request.user.username
        voted = MonkeyIsVoted.objects.create(user=user, is_voted=True)
        voted.save()
        return redirect('result')
    else:
        form = MonkeyForm()
        data = {
            'executors': executors,
            'form': form,
            'isVoted': isVoted,
        }

        return render(request, 'method.html', data)


def ExpertMethod(request):
    executors1 = Executor.objects.all().order_by('-id')[1]
    executors2 = Executor.objects.all().order_by('-id')[2]
    executors3 = Executor.objects.all().order_by('-id')[3]
    expert = [0.14, 0.69, 0.17]
    marks = MethodMarks.objects.all()
    i = 0
    j = 0
    for mark in marks:
        Monkey[i][j] = mark.mark1 * expert[i]
        i += 1
        Monkey[i][j] = mark.mark2 * expert[i]
        i += 1
        Monkey[i][j] = mark.mark3 * expert[i]
        i = 0
        j += 1
    result1 = Monkey[0][0] + Monkey[1][0] + Monkey[2][0]
    result2 = Monkey[0][1] + Monkey[1][1] + Monkey[2][1]
    result3 = Monkey[0][2] + Monkey[1][2] + Monkey[2][2]
    if result1 > result2 and result1 > result3:
        result = result1
        answer = 1
    elif result2 > result1 and result2 > result3:
        result = result2
        answer = 2
    else:
        result = result3
        answer = 3
    data = {
        'result': result,
        'answer': answer,
        'executor1': executors1,
        'executor2': executors2,
        'executor3': executors3,
    }

    return render(request, 'method_result.html', data)
