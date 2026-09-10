from django.shortcuts import render, redirect

from .models import Task


def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            return redirect('task_list')

    tasks = Task.objects.all()
    return render(request, 'todos/task_list.html', {'tasks': tasks})

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            task.title = title
            task.save()
            return redirect('task_list')

    return render(request, 'todos/edit_task.html', {'task': task})



