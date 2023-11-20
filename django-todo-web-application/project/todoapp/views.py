from django.shortcuts import render, redirect
from .models import Task


# Create your views here.
def homepage(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')

        task = Task(name=name, priority=priority)
        task.save()
        redirect('/')
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})
