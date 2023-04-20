from django.shortcuts import render, redirect
from datetime import datetime
from .forms import LoginForm


def index(request):
    return render(request, 'index.html', {'current_date_time': datetime.now})


def login(request):
    form = LoginForm()
    return render(request, 'login.html')