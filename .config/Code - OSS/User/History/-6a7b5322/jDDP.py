from django.shortcuts import render
from django.views.generic.list import ListView


class TaskList(ListView):
    model = Task