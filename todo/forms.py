from django import forms
from .models import TodoModel


class EditTodoModelForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['task_name', 'description']


class CreateTodoModelForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['task_name', 'description']
