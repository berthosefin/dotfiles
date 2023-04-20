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


def update(request, pk):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted

    todo.save()
    return redirect('todos:index')