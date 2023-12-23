from django.shortcuts import render,redirect
from .forms import CatagoryForm
# Create your views here.

def add_catagory(request):
    if request.method=='POST':
        catagory= CatagoryForm(request.POST)
        if catagory.is_valid():
            print(catagory.cleaned_data)
            catagory.save()
            return redirect('add_catagory')
            
    catagory= CatagoryForm()
    return render(request,'add_category.html', {'form':catagory})
            
