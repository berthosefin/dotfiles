from django.shortcuts import render
from django.views.generic.list import ListView


class TaskList(ListView):
    return HttpResponse(' To Do List ')