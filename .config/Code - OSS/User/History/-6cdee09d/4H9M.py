from django.shortcuts import render
from datetime import datetime


def welcome(request):
    return render(request, 'trombinoscoop/welcome.html')