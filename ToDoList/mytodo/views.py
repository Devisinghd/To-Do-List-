from django.shortcuts import render, redirect
from .models import Jobs 
from .forms import tasksForm
# Create your views here.
def main(request):
    tasks = Jobs.objects.all().order_by('-time')
    return render(request,'myapp/index.html',{'tasks':tasks})

def detail(request,id):
    task = Jobs.objects.get(id=id)
    return render(request,'myapp/detail.html',{'task':task})

def add_task(request):
    form = tasksForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('mytodo:main')
    else:
        form = tasksForm()
    return render(request,'myapp/add-task.html',{'form':form})

def edit_task(request,id):
    task = Jobs.objects.get(id=id)
    form = tasksForm(request.POST or None,instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('mytodo:main')
    return render(request,'myapp/add-task.html',{'form':form})

def delete_task(request,id):
    task = Jobs.objects.get(id=id)
    task.delete()
    return redirect('mytodo:main')


