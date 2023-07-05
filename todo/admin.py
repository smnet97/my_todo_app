from django.contrib import admin
from .models import TodoModel, CategoryModel


admin.site.register(CategoryModel)


@admin.register(TodoModel)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'task_name', 'created_at', 'task_status']
    list_display_links = ['id', 'task_name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['task_name']
