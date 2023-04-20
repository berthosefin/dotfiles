from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.core import exceptions
from .models import Person, Student, Employee, Message
from .forms import LoginForm, StudentProfileForm, EmployeeProfileForm, AddFriendForm


def index(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        if 'newMessage' in request.GET and request.GET['newMessage'] != '':
            newMessage = Message(author=logged_user, content=request.GET['newMessage'], publication_date = date.today())
            newMessage.save()
        friendMessages = Message.objects.filter(author__friends=logged_user).order_by('-publication_date')
        return render(request, 'base/index.html', {'logged_user': logged_user, 'friendMessages': friendMessages})
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


def get_logged_user_from_request(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        # On cherche un etudiant
        if len(Student.objects.filter(id=logged_user_id)) == 1:
            return Student.objects.get(id=logged_user_id)
        # On cherche un employe
        elif len(Employee.objects.filter(id=logged_user_id)) == 1:
            return Employee.objects.get(id=logged_user_id)
        # Si on n'a rien trouve
        else:
            return None
    else:
        return None


def add_friend(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        # Test si le formulaire a été envoyé
        if len(request.GET) > 0:
            form = AddFriendForm(request.GET)
            if form.is_valid():
                new_friend_email = form.cleaned_data['email']
                newFriend = Person.objects.get(email=new_friend_email)
                logged_user.friends.add(newFriend)
                logged_user.save()
                return redirect('index')
            else:
                return render(request, 'base/add_friend.html', {'form': form})
        # Le formulaire n'a pas été envoyé
        else:
            form = AddFriendForm()
            return render(request, 'base/add_friend.html', {'form': form})
    else:
        return redirect('login')


def show_profile(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        # Teste si le paramètre attendu est bien passé
        if 'userToShow' in request.GET and request.GET['userToShow'] != '':
            user_to_show_id = int(request.GET['userToShow'])
            results = Person.objects.filter(id=user_to_show_id)
            if len(results) == 1:
                if Student.objects.filter(id=user_to_show_id):
                    user_to_show = Student.objects.get(id=user_to_show_id)
                else:
                    user_to_show = Employee.objects.get(id=user_to_show_id)
                return render(request, 'base/show_profile.html', {'user_to_show': user_to_show})
            else:
                return render(request, 'base/show_profile.html', {'user_to_show': user_to_show})
        # Le paramètre n'a pas été troué
        else:
            return render(request, 'base/show_profile.html', {'user_to_show': logged_user})
    else:
        return redirect('login')


def modify_profile(request):
    logged_user = get_logged_user_from_request(request)
    if logged_user:
        if len(request.GET) > 0:
            if type(logged_user) == Student:
                form = StudentProfileForm(request.GET, instance=logged_user)
            else:
                form = EmployeeProfileForm(request.GET, instance=logged_user)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                return render(request, 'base/modify_profile.html', {'form': form})
        else:
            if type(logged_user) == Student:
                form = StudentProfileForm(instance=logged_user)
            else:
                form = EmployeeProfileForm(instance=logged_user)
            return render(request, 'base/modify_profile.html', {'form': form})
    else:
        return redirect('login')


def ajax_check_email_field(request):
    html_to_return = ''
    if 'value' in request.GET:
        field = forms.EmailField()
        try:
            field.clean(request.GET['value'])
        except forms.ValidationError as ve:
            html_to_return = '<ul class="errorlist">'
            for message in ve.messages:
                html_to_return += '<li>' + message + '</li>'
            html_to_return += '<ul>'
        
        if len(html_to_return) == 0:
            if len(Person.objects.filter(email=request.GET['value'])) >= 1:
                html_to_return = '<ul class="errorlist">'
                html_to_return += '<li>Cette addresse est déjà utilisée!</li>'
                html_to_return += '</ul>'
    return HttpResponse(html_to_return)