from django.shortcuts import render

from .models import Todo

def index(request):
    todos = Todo.objects.all()
    context = ({'todos': todos})

    if request.method == "POST":
        todo = Todo.objects.get(id = request.POST['todoid'])
        todo.completed = not todo.completed
        todo.save()


    return render(request, 'todo/index.html', context)

