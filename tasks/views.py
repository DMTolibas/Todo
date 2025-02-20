from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task
from .forms import TaskForm

def index(request):

    form = TaskForm()

    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():

            form.save()

        return redirect('/')

    context = {'tasks': tasks, 'TaskForm': form}

    return render(request, 'index.html', context)


def updateTask(request, pk):

    task = Task.objects.get(id=pk) #get the obj ID

    form = TaskForm(instance=task) #fill the label with the current task you selected

    if request.method == 'POST': #check if the user want to send a data

        form = TaskForm(request.POST, instance=task) #update the specific task with the new data that the user provided . Both select the previous data and the new data

        if form.is_valid():

            form.save()

            return redirect('/')
        
    context = {'TaskForm': form}

    return render(request, 'update-task.html', context)
