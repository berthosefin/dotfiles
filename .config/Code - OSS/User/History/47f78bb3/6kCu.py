from django.urls import path
from .views import home, room, create_room, update_room

urlpatterns = [
    path('', home, name='home'),
    path('room/<str:pk>/', room, name='room'),
    path('create-room/', create_room, name='create-room'),
    path('update-room/', update_room, name='update-room'),
]