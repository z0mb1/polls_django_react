from django.contrib.auth import authenticate, login
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls import url

from users import views

app_name = 'users'
urlpatterns = [
    # Страница регистрации
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
]
