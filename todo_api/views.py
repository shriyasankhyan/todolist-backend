from rest_framework import generics
from .serializers import TaskSerializer

class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer
