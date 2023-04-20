from django.contrib import admin
from tasks.models import Task, Collection


admin.site.register(Task)
admin.site.register(Collection)