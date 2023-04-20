from django.shortcuts import render, redirect
from datetime import datetime
from .forms import LoginForm, StudentProfileForm, EmployeeProfileForm


def index(request):
    return render(request, 'base/index.html', {'current_date_time': datetime.now})


def login(request):
    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('index')
        else:
            return render(request, 'base/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'base/login.html', {'form': form})

def register(request):
    if len(request.GET) > 0 and 'profileType' in request.GET:
        studentForm = StudentProfileForm(prefix='st')
        employeeForm = StudentProfileForm(prefix='em')
        if request.GET['profileType'] == 'student':
            studentForm = StudentProfileForm(request.GET, prefix='st')
            if studentForm.is_valid():
                studentForm.save()
                return redirect('login')
        elif request.GET['profileType'] == 'employee':
            studentForm = StudentProfileForm(request.GET, prefix='st')
            if studentForm.is_valid():
                studentForm.save()
                return redirect('login')
        else:
            return render(request, 'base/user_profile.html', {'form': form})
    else:
        form = StudentProfileForm()
        return render(request, 'base/user_profile.html', {'form': form})