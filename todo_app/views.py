from django.shortcuts import render, redirect,get_object_or_404
from . models import ToDoItem


# Create your views here.
def todo_list(request):
    todos = ToDoItem.objects.all()
    return render(request,'todo_list.html',{'todos':todos})

#to do creation 
def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        # create todo objects to save it DB
        ToDoItem.objects.create(
            title  = title ,
            description = description
        )

        #return to todo list
        return redirect('todo_list')
    return render(request,'todo_form.html')


#update tasks
def update_todo(request, id):
    todo = get_object_or_404(ToDoItem,id=id)

    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.completed = request.POST.get('completed') == 'on'
        todo.save()
        return redirect('todo_list')
    return render(request,'todo_form.html',{'todo':todo})

#deletion operation
def delete_todo(request, id):
    todo = get_object_or_404(ToDoItem,id=id)
    todo.delete()
    return redirect('todo_list')