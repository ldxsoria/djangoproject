from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("Index page")

def hello(resquest, username):
    return HttpResponse('<h1>Hola %s</h1>' %username)

def about(request, username):
    print(username)
    return HttpResponse('<h1>About page</h1>')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    #task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse('tasks %s' % task.title)

