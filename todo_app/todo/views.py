from django.db.models.fields import TimeField
from django.shortcuts import redirect, render

from .models import Todo

def index(request):
    todo_items = Todo.objects.order_by('-created_at')
    context = {
        'todo_items':todo_items
    }
    return render (request,'todo/index.html',context)

def mark_complete(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.is_done = True
    todo.save()
    return redirect('/')

def create_todo(request):
    if request.method == "POST":
        print("running save method")
        new_todo = Todo(desc=request.POST['desc'],title=request.POST['title'])
        new_todo.save()
    return redirect('/')


def remove(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')
