from django.shortcuts import render, redirect, get_object_or_404
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


def update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    is_completed = request.POST.get('is_completed', False)
    if is_completed == 'on':
        is_completed = True
    todo.is_completed = is_completed
    todo.save()
    return redirect('todos:index')