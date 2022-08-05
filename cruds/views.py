from asyncio import tasks
from turtle import title
from django.shortcuts import render, redirect

import cruds
from .models import Task

# Create your views here.
def list_crud1(request):
     cruds = Task.objects.all()
     print(cruds)
     return render(request, "list_crud1.html",{"cruds": cruds })
 
def create_task(request):
    new_title = request.POST["title"]
    new_description = request.POST["description"]
    if new_title == "" or new_description == "":
        tasks = Task.objects.all()
        return render(
            request, "list_tasks.html", {"tasks": tasks, "error": "Title and description is required"}
        )
    task = Task(title=new_title, description=new_description)
    task.save()
    return redirect("/cruds/")

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("/cruds/")