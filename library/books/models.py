from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
