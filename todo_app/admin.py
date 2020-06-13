from django.contrib import admin

from . import models


@admin.register(models.TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'completed', 'deleted')
    list_filter = ('deleted', 'completed')
    date_hierarchy = 'created_at'
