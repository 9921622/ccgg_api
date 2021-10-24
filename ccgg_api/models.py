from django.db import models
from datetime import datetime

# Create your models here.
class Pawn(models.Model):
    name = models.CharField(max_length=60)
    pawn = models.CharField(max_length=30, default="Unknown")
    date = models.DateTimeField(default=datetime.now, blank=True)
    data = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.name

class Turtle(models.Model):
    name = models.CharField(max_length=60)
    command = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.name
