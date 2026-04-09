from django.shortcuts import render
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
    form = tasksForm()
    return render(request,'myapp/add-task.html',{'form':form})

def update_task(request,id):
    return render(request, 'myapp/update-task',{'task':task})