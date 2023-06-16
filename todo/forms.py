from django.forms import ModelForm
from .models import TodoModel


class CreateTodoModelForm(ModelForm):
    class Meta:
        model = TodoModel
        fields = ['task_name', 'description']
