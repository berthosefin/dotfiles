from django.shortcuts import render


def welcome(request):
    return render(request, 'trombinoscoop/welcome.html')