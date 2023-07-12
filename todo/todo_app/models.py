# todos/models.py
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def _str__(self):
        return self.title
