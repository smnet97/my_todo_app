from django.shortcuts import render, redirect
from .forms import CreateTodoModelForm
from .models import TodoModel


def todo_list_view(request):
    todos = TodoModel.objects.all()
    return render(request, 'main/todo_list.html', context={
        'tasks': todos
    })


def todo_create_view(request):
    form = CreateTodoModelForm()
    if request.method == 'POST':

        form = CreateTodoModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')

    return render(request, 'main/todo_create.html', context={
        'create_form': form
    })
