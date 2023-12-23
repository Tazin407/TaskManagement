from django.shortcuts import render, redirect
from task.models import TaskModel

def home(request):
    task= TaskModel.objects.all()
    return render(request, 'home.html', {'task':task})