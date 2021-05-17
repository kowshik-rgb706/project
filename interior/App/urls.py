from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('about/', views.about),
    path('services/', views.services),
    path('price/', views.price),
    path('projects/', views.projects),
    path('contact/', views.contact),
    path('home/', views.Home),
    path('register/', views.register),
    path('login/', views.login),
    path('register/reg_done/', views.reg_done),
    path('login/login_done/', views.login_done),

]