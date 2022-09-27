from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project
from .models import Task

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

def tasks(request):
    return HttpResponse('tasks')

