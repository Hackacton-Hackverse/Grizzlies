from django.urls import path
from .views import task_list,create_task,update_task,delete_task,select_task

urlpatterns = [
    # path('',index,name='index'),
    path('', task_list, name = 'task-list'),
    path('create/', create_task, name = 'create-task'),
    path('update-<str:task_title>/', update_task, name = 'update-task'),
    path('delete-<str:task_title>/', delete_task, name = 'delete-task'),
    path('selected-<str:objet>/', select_task,name = 'selected-task'),

]
