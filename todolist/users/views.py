from django.shortcuts import render,redirect
from .forms import UserLoginForm,UserRegisterForm,AddTask
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from tasks.models import Task
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('tasks:tasks_list')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        print(request.POST)
        form = UserLoginForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password)
            if user != None:
                auth.login(request, user)
                return redirect('tasks:tasks_list')
      

            else:
                form.add_error(None, "Неверное имя пользователя или пароль")
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    auth.logout(request)
    return redirect('users:register')

@login_required
def profile(request):
    if request.method == "POST":
        form = AddTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('users:profile')
        else:
            print(form.errors)
    else:
        form = AddTask()
    
    # Получаем задачи пользователя
    done_tasks = Task.objects.filter(user=request.user, is_done=True)
    undone_tasks = Task.objects.filter(user=request.user, is_done=False)

    context = {
        'form': form,
        'done_tasks': done_tasks,
        'undone_tasks': undone_tasks,
    }
    return render(request, "users/profile.html", context)