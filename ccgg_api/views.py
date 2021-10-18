from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TurtleSerializer
from .models import Turtle
# Create your views here.


class TurtleViewSet(viewsets.ModelViewSet):
    queryset = Turtle.objects.all().order_by("name")
    serializer_class = TurtleSerializer
