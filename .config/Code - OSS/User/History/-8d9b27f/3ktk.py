from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateField('Created', auto_now_add=True)
    updated_at = models.DateField('Updated', auto_now=True)
    is_completed = models.BooleanField(default=False)