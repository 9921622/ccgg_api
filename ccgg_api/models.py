from django.db import models
from datetime import datetime

# Create your models here.
class Pawn(models.Model):
    identifier = models.CharField(max_length=15, default="")
    date = models.DateTimeField(default=datetime.now, blank=True)
    data = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.identifier

class Turtle(models.Model):
    name = models.CharField(max_length=60)
    command = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.name
