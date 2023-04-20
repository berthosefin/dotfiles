from django.shortcuts import render


def index(request):
    render(request, 'store/index.html')

