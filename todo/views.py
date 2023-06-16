from django.shortcuts import render


def todo_list_view(request):
    return render(request, 'main/todo_list.html')


def create_todo_view(request):
    pass
