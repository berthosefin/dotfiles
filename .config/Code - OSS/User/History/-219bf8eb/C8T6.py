from django.shortcuts import render, redirect
from datetime import datetime
from .models import Person, Student, Employee
from .forms import LoginForm, StudentProfileForm, EmployeeProfileForm


def index(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        logged_user = Person.objects.get(id=logged_user_id)
        return render(request, 'base/index.html', {'logged_user': logged_user})
    else:
        return redirect('login')


def login(request):
    # Teste si le formulaire a été envoyé.
    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            logged_user = Person.objects.get(email=user_email)
            request.session['logged_user_id'] = logged_user.id
            return redirect('index')
        else:
            return render(request, 'base/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'base/login.html', {'form': form})


def register(request):
    if len(request.GET) > 0 and 'profileType' in request.GET:
        studentForm = StudentProfileForm(prefix='st')
        employeeForm = EmployeeProfileForm(prefix='em')
        if request.GET['profileType'] == 'student':
            studentForm = StudentProfileForm(request.GET, prefix='st')
            if studentForm.is_valid():
                studentForm.save()
                return redirect('login')
        elif request.GET['profileType'] == 'employee':
            employeeForm = EmployeeProfileForm(request.GET, prefix='em')
            if employeeForm.is_valid():
                employeeForm.save()
                return redirect('login')
        return render(request, 'base/user_profile.html', {'studentForm': studentForm, 'employeeForm': employeeForm})
    else:
        studentForm = StudentProfileForm(prefix='st')
        employeeForm = EmployeeProfileForm(prefix='em')
        return render(request, 'base/user_profile.html', {'studentForm': studentForm, 'employeeForm': employeeForm})


def get_logged_user_from_request():
