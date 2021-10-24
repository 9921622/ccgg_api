from django.contrib import admin

from .models import Turtle
from .models import Pawn

# Register your models here.
admin.site.register(Pawn)
admin.site.register(Turtle)
