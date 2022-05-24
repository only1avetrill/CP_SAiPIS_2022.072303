from django.contrib import admin
from django.urls import path
from . import views
from .views import ExecutorDetail

urlpatterns = [
    path('ad/sort/<slug:sort_slug>', views.sortAds, name='sortAds'),
    path('executor/sort/<slug:sort_slug>', views.sortExecutors, name='sortExecutors'),
    path('about', views.AboutPage, name='about'),
    path('main', views.MainPage, name='main'),
    path('register', views.RegisterUser, name='register'),
    path('executors', views.ExecutorsPage, name='executors'),
    path('analytics', views.AnalyticsPage, name='analytics'),
    path('add_ad', views.AddAdsPage, name='addad'),
    path('add_executor', views.AddExecutorsPage, name='addexec'),
    path('add_ad_error', views.AddAdsError, name='aderror'),
    path('add_executor_error', views.AddExecutorsError, name='execerror'),
    path('add_success', views.AddSuccess, name='addsuccess'),
    path('', views.LoginUser.as_view(), name="auth"),

    path('deleteexecutor/<int:id>', views.DeleteExecutor),
    path('editexecutor/<int:id>', views.EditExecutor),

    path('deletead/<int:id>', views.DeleteAd),
    path('editad/<int:id>', views.EditAd),

    path('executors/<pk>', ExecutorDetail.as_view(), name='exec_details'),

    path('loginrequired', views.LoginRequired, name="loginrequired"),

    path('logout', views.logout_user, name="logout"),
]
