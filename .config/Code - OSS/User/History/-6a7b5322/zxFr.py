from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task


class TaskList(ListView):
    model = Task