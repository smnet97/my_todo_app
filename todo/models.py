from django.db import models


class TodoModel(models.Model):
    task_name = models.CharField(max_length=255)
    description = models.TextField()
    task_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
        ordering = ['-created_at']
