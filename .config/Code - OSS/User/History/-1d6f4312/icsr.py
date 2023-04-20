from django.shortcuts import render

# Create your views here.
def add_n_show(request):
    return render(request, 'student/add_n_show.html')
