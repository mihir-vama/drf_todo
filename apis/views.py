from rest_framework import viewsets
from rest_framework.response import Response

from todos.models import Todo, User
from .serializers import TodoSerializer, UserSerializers

from rest_framework.renderers import JSONRenderer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("admin_id")
        if user_id:
            return Todo.objects.filter(user_id=user_id)
        return Todo.objects.all()



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()

