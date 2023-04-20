from django.shortcuts import render, redirect
from datetime import datetime


def welcome(request):
    return render(request, 'welcome.html', {'current_date_time': datetime.now})


def login(request):
    if len(request.POST) >0:
        if 'email' not in request.POST or 'password' not in request.POST:
            error = "Veuillez entrer une addresse email et un mot de passe."
            return render(request, 'login.html', {'error': error})
        else:
            email = request.POST['email']
            password = request.POST['password']
    else:
        return render(request, 'login.html')