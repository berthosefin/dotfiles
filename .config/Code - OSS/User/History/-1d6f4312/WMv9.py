from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_n_show(request):
    if request.method == 'POST':
        f = StudentRegistration(request.POST)
        if f.is_valid():
            f.save()
    else:
        f = StudentRegistration()
    return render(request, 'student/add_n_show.html', {'form': f})
