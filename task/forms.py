from django import forms
from .import models

class TaskForm(forms.ModelForm):
    class Meta:
        model= models.TaskModel
        fields="__all__"
        labels={
            'title': 'Title',
            'description': 'Task Description',
            'assign_date': 'Assigned Date',
            
        }
        
        widgets={
            'assign_date': forms.DateInput(attrs={'type':'date'}),
            'catagory': forms.CheckboxSelectMultiple
        }