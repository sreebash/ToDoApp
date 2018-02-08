from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST

# Create your views here.


def home(request):
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()
    context = {'todo_list':todo_list, 'form':form}
    return render(request, 'todo/home.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
    print(request.POST['text'])
    return redirect('home')


def todoComplete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('home')


def deleteCompleted(request):
    todo = Todo.objects.filter(complete=True)
    todo.delete()
    return redirect('home')

def deleteAll(request):
    todo = Todo.objects.all()
    todo.delete()
    return redirect('home')