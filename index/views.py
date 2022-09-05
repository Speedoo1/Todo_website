from django.shortcuts import render, redirect

# Create your views here.
from index.form import TodoForm
from index.models import Todo_App


def task_list(request):
    form = TodoForm
    task = Todo_App.objects.all().order_by('-date_created')

    context = {'form': form, 'tasks': task}
    return render(request, 'index/task_list.html', context)


def addlist(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
    if form.is_valid:
        form.save()
        return redirect('todo:list')


def taskComplete(request, pk):
    task = Todo_App.objects.get(id=pk)

    task.Task_done = True
    if task:
        task.save()

    return redirect('todo:list')


def taskDelete(request, pk):
    task = Todo_App.objects.get(id=pk)
    task.delete()
    return redirect('todo:list')
