from django.db import models

# Create your models here.
class Turtle(models.Model):
    name = models.CharField(max_length=60)
    command = models.CharField(max_length=300)
    from_turtle = models.BooleanField()

    def __str__(self):
        return self.name
