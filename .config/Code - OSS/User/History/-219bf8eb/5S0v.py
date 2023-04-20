from django.shortcuts import render, redirect
from datetime import datetime
from .models import Person
from .forms import LoginForm, StudentProfileForm, EmployeeProfileForm


def index(request):
    return render(request, 'base/index.html', {'current_date_time': datetime.now})


def login(request):
    # Teste si le formulaire a été envoyé.
    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            logged_user = Person.objects.get(email=user_email)
            request.session['logged_user_id'] = logged_user.id
            return redirect('welcome')
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