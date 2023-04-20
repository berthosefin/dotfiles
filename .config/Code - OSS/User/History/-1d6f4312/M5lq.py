from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_n_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            register = User(name = name, email = email, password = password)
            register.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration()
    students = User.objects.all()
    return render(request, 'student/add_n_show.html', {'form': form, 'students': students})


def delete(request, id):
    if request.method == 'POST':
        student = User.objects.get(pk=id)
