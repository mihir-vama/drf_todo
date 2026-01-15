from rest_framework import serializers
from todos.models import Todo, User


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "description",
            "user"
        )
        model = Todo


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "username",
            "password",
        )
        model = User

