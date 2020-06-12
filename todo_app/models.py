from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=1024)
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
