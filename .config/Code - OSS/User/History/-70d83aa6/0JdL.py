from django.shortcuts import render
from django.contrib.auth.models import get_user_model


User = get_user_model()

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)

    return render(request, 'accounts/signup.html')
