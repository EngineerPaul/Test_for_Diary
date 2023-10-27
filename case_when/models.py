from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=20, blank=True)
    number = models.IntegerField()
