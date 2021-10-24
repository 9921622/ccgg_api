from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TurtleSerializer
from .models import Turtle
# Create your views here.


class TurtleViewSet(viewsets.ModelViewSet):
    queryset = Turtle.objects.all().order_by("name")
    serializer_class = TurtleSerializer

    def get_object(self, pk):
        return Turtle.objects.get(pk=pk)
    
    def patch(self, request, pk):
        model_object = self.get_object(pk)
        serializer = TurtleSerializer(model_object, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(code=400, data="wrong parameters")
