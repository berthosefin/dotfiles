from django.urls import path
from .views import index, loginn register


urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]