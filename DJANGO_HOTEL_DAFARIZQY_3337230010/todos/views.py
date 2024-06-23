# todos/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo

class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all the todos ordered by their id."""
        return Todo.objects.order_by('-id')

def add(request):
    title = request.POST['title']
    Todo.objects.create(title=title)
    return redirect('todos:index')

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('todos:index')

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    todo.isCompleted = isCompleted
    todo.save()
    return redirect('todos:index')

def edit(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.save()
        return redirect('todos:index')
    return render(request, 'todos/edit.html', {'todo': todo})
