from django.contrib import admin

from . import models


@admin.register(models.TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed', 'deleted')
    list_filter = ('deleted', 'completed')
