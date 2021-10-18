from django.db import models

# Create your models here.
class Turtle(models.Model):
    name = models.CharField(max_length=60)
    last_ping = models.DateField()
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()

    def __str__(self):
        return self.name
