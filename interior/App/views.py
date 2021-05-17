from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from . import models
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

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def reg_done(request):
    regobj = models.Register()

    name = request.POST.get('name')
    mail = request.POST.get('mail')
    psw = request.POST.get('psw')
    pswr = request.POST.get('pswr')
    all = [name, mail, psw, pswr]


    regobj.name = name
    regobj.mail = mail
    regobj.psw = psw
    regobj.pswr = pswr
    regobj.save()

    return render(request, 'reg_done.html')

def login_done(request):
    regobj = models.Register()

    lmail = request.POST.get('lmail')
    lpsw = request.POST.get('lpsw')


    lmail = regobj.mail
    lpsw = regobj.psw

    if lmail is not None:
        return render(request, 'login_done.html',)
    else:
        return render(request, 'sorry.html',)


