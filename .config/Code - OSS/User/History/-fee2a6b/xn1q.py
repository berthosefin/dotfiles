from django.shortcuts import render
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'todos/index.html'