from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('about/', views.about),
    path('services/', views.services),
    path('price/', views.price),
    path('projects/', views.projects),
    path('contact/', views.contact),
    path('register/', views.register),
    path('login/', views.loginpage),
    path('home/', views.Home, name='home'),
    path('About1/', views.About1),
    path('Services1/', views.Services1),
    path('Price1/', views.Price1),
    path('Projects1/', views.Projects1),
    path('Contact1/', views.Contact1),
    path('logoutUser/', views.logoutUser)

]