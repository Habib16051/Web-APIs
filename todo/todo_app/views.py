from django.shortcuts import render
from . models import Todo
from .serializers import TodoSerializers
from rest_framework import generics


# For displaying all the list of todos
class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


# for displaying individual details of a todos
class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
