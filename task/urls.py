from django.urls import path,include
from .import views

urlpatterns = [
    
    path('',views.add_task, name='add_task'),
    path('edit_task/<int:id>',views.edit_task, name='edit_task'),
    path('delete_task/<int:id>',views.delete_task, name='delete_task'),
    path('complete_task/<int:id>',views.complete_task, name='complete_task'),
]
