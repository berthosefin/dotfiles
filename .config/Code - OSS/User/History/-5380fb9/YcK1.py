from django.urls import path
from .views import index, login, register, add_friend, show_profile


urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('addFriend/', add_friend, name='addFriend'),
]