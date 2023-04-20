from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_n_show(request):
    if request.method == 'POST':
        f = StudentRegistration(request.POST)
        if f.is_valid():
            nom = f.clean_data['name']
            mail = f.clean_data['email']
            passwd = f.clean_data['password']
            reg = User(name = nom, email = mail, password = passwd)
            reg.save()
            f = StudentRegistration()
    else:
        f = StudentRegistration()
    return render(request, 'student/add_n_show.html', {'form': f})
