from django.shortcuts import render, redirect
from django.views import generic
from .models import Todo


class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todos'

    def get_queryset(self):
        # Return all the latest todos.
        return Todo.objects.order_by('-created_at')


def add(request):
    title = request.POST['title']
    Todo.objects.create(title=title)

    return redirect('todos:index')