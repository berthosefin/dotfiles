from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_n_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = f.clean_data['name']
            email = f.clean_data['email']
            password = f.clean_data['password']
            register = User(name = name, email = email, password = password)
            register.save()
    else:
        form = StudentRegistration()
    return render(request, 'student/add_n_show.html', {'form': form})
