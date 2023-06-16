from django.urls import path
from .views import todo_list_view

urlpatterns = [
    path('', todo_list_view, name='todo_list')
]
