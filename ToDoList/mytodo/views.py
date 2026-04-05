from django.shortcuts import render
from .models import Jobs 
# Create your views here.
def main(request):
    tasks = Jobs.objects.all().order_by('-time')
    return render(request,'myapp/index.html',{'tasks':tasks})
