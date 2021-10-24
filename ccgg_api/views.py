from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import PawnSerializer
from .serializers import TurtleSerializer

from .models import Pawn
from .models import Turtle

# Create your views here.

class PawnViewSet(viewsets.ModelViewSet):
    queryset = Pawn.objects.all().order_by("date")
    serializer_class = PawnSerializer

##    def get_object(self, pk):
##        return Pawn.objects.get(pk=pk)
##    
##    def delete(self, request, *args, **kwargs):
##        pk = self.kwargs.get("pk")
##        model_object = self.get_object(pk)
##        model_object.delete()
##        return HttpResponse(204)
        
    
    
class TurtleViewSet(viewsets.ModelViewSet): # if post request response should be its pk?
    queryset = Turtle.objects.all().order_by("name")
    serializer_class = TurtleSerializer


##    def get_object(self, pk):
##        return Turtle.objects.get(pk=pk)
##
##
##    def put(self, request, *args, **kwargs):
##        pk = self.kwargs.get("pk")
##        model_object = self.get_object(pk)
##        serializer = TurtleSerializer(model_object, data=request.data)
##        
##        if serializer.is_valid():
##            serializer.save()
##            return JsonResponse(code=201, data=serializer.data)
##        return JsonResponse(code=400, data="wrong parameters")
##
##        
##    def patch(self, request, *args, **kwargs):
##        pk = self.kwargs.get("pk")
##        model_object = self.get_object(pk)
##        serializer = TurtleSerializer(model_object, data=request.data, partial=True)
##
##        if serializer.is_valid():
##            serializer.save()
##            return JsonResponse(code=201, data=serializer.data)
##        return JsonResponse(code=400, data="wrong parameters")

    
