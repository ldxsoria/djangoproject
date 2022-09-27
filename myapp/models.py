from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    #Esto une una tarea a un proyeco y con CASCADE
    #elimino la tarea, si se elimina el proyecto
    project = models.ForeignKey(Project, on_delete=models.CASCADE)