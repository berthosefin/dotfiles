from django.urls import path
from .views import index, login, register, add_friend


urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]