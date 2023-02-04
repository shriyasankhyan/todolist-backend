from rest_framework import serializers
from .models import Todo

class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Todo
        fields = ["title", "description", "iscompleted", "deadline"]

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
