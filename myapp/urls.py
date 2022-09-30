from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
    path('hello/', views.hello),
	path('about/', views.about),
    path('projects/', views.projects),
    path('create_project', views.create_project),
    path('tasks/', views.tasks),
    path('create_task/', views.create_task),
]
