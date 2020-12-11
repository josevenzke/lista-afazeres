from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context_dict={'tasks':tasks,'form':form}
    return render(request, 'tasks/index.html',context_dict)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context_dict = {'form':form}
    return render(request,'tasks/atualizar.html',context_dict)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    context_dict = {'item':item}
    return render(request, 'tasks/deletar.html',context_dict)
