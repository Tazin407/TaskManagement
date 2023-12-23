from django.db import models
from category.models import TaskCategory
from datetime import date

# Create your models here.
class TaskModel(models.Model):
    title= models.CharField(max_length=100)
    description= models.TextField()
    is_completed= models.BooleanField(default=False)
    assign_date=models.DateField(default= date.today)
    catagory= models.ManyToManyField(TaskCategory)
    
    def __str__(self):
        return self.title
    
    
    
   
