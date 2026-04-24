from django.contrib import admin
# Register your models here.
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'priority', 'completed', 'created_at')
    list_filter = ('completed', 'priority')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
