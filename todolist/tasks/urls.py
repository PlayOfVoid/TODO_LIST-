from django.urls import path
from . import views as task


app_name = 'tasks'


urlpatterns = [
    path('',task.tasks_list,name='tasks_list'),
    path('task_is_done/<int:task_id>/',task.task_is_done,name='task_is_done'),
]