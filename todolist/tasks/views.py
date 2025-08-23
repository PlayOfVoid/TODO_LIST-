from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Task
# from django.contrib.auth.models import User
# Create your views here.

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

   
    