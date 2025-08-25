from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Task
# from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request,"tasks/index.html")

@login_required
def tasks_list(request):
    user = request.user
    print(user)
    tasks = Task.objects.filter(user=user)
    print(tasks)

    context = {
        'tasks':tasks,
    }
    return render(request,"tasks/tasks_list.html",context)


def task_is_done(request,task_id):
    task = get_object_or_404(Task,pk=task_id)
    if task.is_done == False:
        task.is_done = True
        task.save()
        
    else:
        task.is_done = False
        task.save()
        
    return redirect('tasks:tasks_list')

   
    
def detail_task(request,task_id):

    task = get_object_or_404(Task,pk=task_id)
    context = {
        'task':task
    }


    return render(request,"tasks/detail_task.html",context)