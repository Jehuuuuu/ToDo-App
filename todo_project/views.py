from django.shortcuts import render
from todo.models import Task
from django.http import HttpResponse
def get_or_create_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def home(request):
    session_key = get_or_create_session_key(request)
    if session_key:
        tasks = Task.objects.filter(session_key = session_key, is_completed=False).order_by('-updated')
        completed_task = Task.objects.filter(session_key = session_key, is_completed=True)
        return render(request, 'home.html', {'tasks': tasks, 'completed_task': completed_task})
    return HttpResponse("Error creating session")
