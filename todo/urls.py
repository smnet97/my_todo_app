from django.urls import path
from .views import todo_list_view, todo_create_view, todo_delete_view, todo_detail_view, todo_edit_view, todo_check_view

urlpatterns = [
    path('', todo_list_view, name='todo_list'),
    path('todo/create/', todo_create_view, name='todo_create'),
    path('todo/delete/<int:id>/', todo_delete_view, name='todo_delete'),
    path('todo/detail/<int:id>/', todo_detail_view, name='todo_detail'),
    path('todo/edit/<int:id>/', todo_edit_view, name='todo_edit'),
    path('todo/check/<int:id>/', todo_check_view, name='todo_check')
]
