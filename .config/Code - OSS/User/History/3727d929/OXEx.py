from django.shortcuts import render

# Create your views here.

rooms = [
    {id: 1, 'name': 'Lets leran python!'},
    {id: 2, 'name': 'Design with me'},
    {id: 3, 'name': 'Frontend developpers'},
]

def home(request):
    return render(request, 'home.html', {'rooms': rooms})


def room(request):
    return render(request, 'room.html')