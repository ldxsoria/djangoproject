from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(resquest):
    return HttpResponse('<h1>Hello World</h1>')

