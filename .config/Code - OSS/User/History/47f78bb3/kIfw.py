from django.urls import path
from .views import home, room

urlpatterns = [
    path('', home, name='home'),
    path('room/<str:pk>/', room, name='room'),
]