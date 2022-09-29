from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
from .forms import CreateNewTask

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(resquest):
    username = 'Diego'
    return render(resquest, 'hello.html', {
        'username':username
    })

def about(request, username):
    print(username)
    return HttpResponse('<h1>About page</h1>')

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html', {
        'projects':projects
    })

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks':tasks
    })

def create_task(request):
    #print(request.GET['title'])
    #print(request.GET['description'])
    Task.objects.create(title=request.GET['title'], description=request.GET['description'], project_id=1)
    return render(request, 'create_task.html', {
        'form': CreateNewTask()
    })
    

