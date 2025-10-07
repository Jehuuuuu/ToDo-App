from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.http import HttpResponse
# Create your views here.
def get_or_create_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def addTask(request):
    session_key = get_or_create_session_key(request)
    if session_key:
        task = request.POST['task']
        if not task:
            return HttpResponse("Missing task name")
       
        Task.objects.create(session_key = session_key, task=task)
        return redirect('home')
    return HttpResponse("Error creating session")

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        context={'task': task}

        return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')

    