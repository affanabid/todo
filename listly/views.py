from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def home(request):
    # if request.method == 'POST':
    #     form = TaskForm(request.POST)
    #     print('fir')
    #     if form.is_valid():
    #         form.save()
    #         print('daved')
    #         return redirect('home')
    # print('unsaved')
    q = request.GET.get('q', '')  # Use an empty string as default if 'q' is not present
    tasks = Task.objects.filter(title__icontains=q)
    return render(request, 'listly/index.html', {'tasks': tasks, 'query': q})

def addTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'listly/form.html', context)

def update_tasks(request, pk):
    tasks = Task.objects.get(id=pk)
    form = TaskForm(instance=tasks)
    print('not post')
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        print('form made')
        if form.is_valid():
            print('formvalid')
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'listly/update_task.html', context)

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {'task':task}
    return render(request, 'listly/delete.html', context)