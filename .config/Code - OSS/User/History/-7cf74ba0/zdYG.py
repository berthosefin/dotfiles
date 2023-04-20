from django.shortcuts import render, redirect
from datetime import datetime
from .forms import LoginForm


def index(request):
    return render(request, 'index.html', {'current_date_time': datetime.now})


def login(request):
    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('index')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})