from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def add_n_show(request):
    if request.method == 'POST':

    return render(request, 'student/add_n_show.html')
