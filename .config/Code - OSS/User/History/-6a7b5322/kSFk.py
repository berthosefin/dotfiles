from django.shortcuts import render
from django.views.generic.list import ListView


class TaskList(request):
    return HttpResponse(' To Do List ')