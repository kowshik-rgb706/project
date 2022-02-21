from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def Index(request):
    return render(request, 'index.html')


def Home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def price(request):
    return render(request, 'price.html')


def projects(request):
    return render(request, 'projects.html')


def contact(request):
    return render(request, 'contact.html')


def About1(request):
    return render(request, 'About1.html')


def Services1(request):
    return render(request, 'Services1.html')


def Price1(request):
    return render(request, 'Price1.html')


def Projects1(request):
    return render(request, 'Projects1.html')


def Contact1(request):
    return render(request, 'Contact1.html')

@unauthenticated_user
def register(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/login')
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form': form})


@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'login.html')

def fromView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'login.html', {"username": username})
    else:return render(request, '/login', {})

def logoutUser(request):
    logout(request)
    return redirect('/login')
