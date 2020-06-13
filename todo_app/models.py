from django.db import models
from django.utils import timezone


class TodoItem(models.Model):
    title = models.CharField(max_length=1024)

    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
