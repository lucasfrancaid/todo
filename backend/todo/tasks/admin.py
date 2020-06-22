from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'done']

admin.site.register(Task, TaskAdmin)
