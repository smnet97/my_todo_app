from django import forms
from .models import TodoModel
from ckeditor.widgets import CKEditorWidget


class EditTodoModelForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['task_name', 'description']


class CreateTodoModelForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['task_name', 'description']
