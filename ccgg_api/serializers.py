from rest_framework import serializers

from .models import Pawn
from .models import Turtle

class PawnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pawn
        fields = ("pk", "identifier", "date", "data")

class TurtleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Turtle
        fields = ("pk", "name", "command")

