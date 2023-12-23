from django.shortcuts import render,redirect
from .forms import TaskForm
from .import models


def add_task(request):
    
    if request.method=="POST":
        task= TaskForm(request.POST)
        if task.is_valid():
            print(task.cleaned_data)
            task.save()
            return redirect('home')
        
    task= TaskForm()
    return render(request,'add_task.html',{'form': task} )
        
def edit_task(request, id):
    
    edited= models.TaskModel.objects.get(pk=id)
    task= TaskForm(instance=edited)
    
    if request.method=='POST':
        edited_task= TaskForm(request.POST, instance=edited)
        if edited_task.is_valid():
            edited_task.save()
            return redirect('home')
        
    return render(request, 'add_task.html', {'form': task})
    
    
def delete_task(request, id):
    deleted= models.TaskModel.objects.get(pk=id)
    deleted.delete()
    return redirect('home')

def complete_task(request, id):
    task= models.TaskModel.objects.get(pk=id)
    task.is_completed=True
    task.save()
    return redirect('home')
    
        
    
            
    
    
