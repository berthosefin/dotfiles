from django.shortcuts import render, redirect
from datetime import datetime


def welcome(request):
    return render(request, 'welcome.html', {'current_date_time': datetime.now})


def login(request):
    return render(request, 'login.html')