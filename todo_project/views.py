from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated')
    completed_task = Task.objects.filter(is_completed=True)


    return render(request, 'home.html', {'tasks': tasks, 'completed_task': completed_task})

