from rest_framework import serializers
from .models import Turtle


class TurtleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Turtle
        fields = ("id", "command")
