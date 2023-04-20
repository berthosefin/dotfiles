from django.urls import path
from .views import TaskList


urlpatterns = [
    path('', views.task_list, name='tasks'),
]