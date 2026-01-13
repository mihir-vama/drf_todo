from rest_framework import generics

from todos import models
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return models.Todo.objects.all()


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return models.Todo.objects.all()
