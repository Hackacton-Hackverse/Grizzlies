from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task
from .forms import TaskForm
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'tasks/index.html')
    
def task_list(request):
    tasks = Task.objects.all()
    #Verification s'il y.a deja des taches
    if not tasks:
        message = "Aucune tache n'a été trouvée"
        context = {'message':message}
    else:
        tasks_non_completed = Task.objects.filter(completed=False)
        tasks_completed = Task.objects.filter(completed=True)
        time_nul = datetime.now().date()-datetime.now().date()
        tasks_completing = Task.objects.filter(time_remaining=time_nul)
        context = {'tasks_n': tasks_non_completed,'tasks': tasks_completed,'tasks_d': tasks_completing}
    
    return render(request, 'tasks/task_list.html',context)


def create_task(request):
    if request.method == 'POST':
           form = TaskForm(request.POST)
           if form.is_valid():
               #Recuperation des infos du form
               title = form.cleaned_data['title'].replace('(','').replace("'","").replace(",","")
               description = form.cleaned_data['description']
               due_date = form.cleaned_data['due_date']
               completed = form.cleaned_data['completed']
               
               #calcul du temps restant
               current_date = datetime.now().date()
               time_remaining = (form.cleaned_data['due_date'] - current_date)
               task = Task(title=title,description=description,completed=completed,due_date=due_date,time_remaining=time_remaining)
               
               #verification si une tache de meme titre exite deja
               if Task.objects.filter(title = title).exists():
                   messages.error(request,'Une tache avec le meme titre existe déjà.Veuillez choisir un titre différent.')
               else:
                   task.save()
                   return redirect('task-list')
    else:
           form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

def update_task(request,task_title):
    task = Task.objects.get(title=task_title)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance = task)
        if form.is_valid():
            #Recuperation des infos du form
               title = form.cleaned_data['title'].replace('(','').replace("'","").replace(",","")
               description = form.cleaned_data['description']
               due_date = form.cleaned_data['due_date']
               completed = form.cleaned_data['completed']
               get_object_or_404(Task,title=task_title).delete()
               #calcul du temps restant
               current_date = datetime.now().date()
               time_remaining = (form.cleaned_data['due_date'] - current_date)
               task = Task(title=title,description=description,completed=completed,due_date=due_date,time_remaining=time_remaining)
               #verification si une tache de meme titre exite deja
               
               if Task.objects.filter(title = title).exists():
                   messages.error(request,'Une tache avec le meme titre existe déjà.Veuillez choisir un titre différent.')
               else:
                   task.save()
                   return redirect('task-list')
    else:
        form = TaskForm(instance = task)
        return render(request, 'tasks/update_task.html', {'form': form , 'task': task})
   
                 
def delete_task(request, task_title):
    task = get_object_or_404(Task,title=task_title)
    if request.method == 'POST':
        #Suppression si la confirmation est recue
        task.delete()
        return HttpResponseRedirect(reverse('task-list')) #Rediriger vers la liste des taches apers la suppression
    return render(request, 'tasks/delete_task.html', {'task':task})

def select_task(request,objet):
    task =Task.objects.all()
    return render(request, 'tasks/select_task.html', {'tasks':task, 'objet':objet})

