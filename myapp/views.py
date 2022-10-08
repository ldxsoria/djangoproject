from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

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
    return render(request, 'projects/projects.html', {
        'projects':projects
    })

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks':tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html',{
            'form':CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect('/tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html',{
            'form':CreateNewProject()
        })
    else:
        project = Project.objects.create(name=request.POST['name'])
        print(project)
        return render(request, 'projects/create_project.html',{
            'form':CreateNewProject()
        })
        
def project_detail(request, id):
    print(id)
    return render(request, 'projects/detail.html')