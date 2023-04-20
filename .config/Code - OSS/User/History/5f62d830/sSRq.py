from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'tasks/index.html', context={})


def add_collection(request):
    return HttpResponse()