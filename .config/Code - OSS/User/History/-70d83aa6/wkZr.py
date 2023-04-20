from django.shortcuts import render


def signup(request):
    render(request, 'accounts/signup.html')
