from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
# from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
# class TodoViewSet(viewsets.ModelViewSet):
#     serializer_class = TodoSerializer
#     queryset = Todo.objects.all()

class TodoListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # For getting all todos
    def get(self, request, *args, **kwargs):
        todos = Todo.objects.filter(user = request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # For creating a todo
    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'isComplete': request.data.get('isComplete'),
            'deadline': request.data.get('deadline'),
            'user': request.user.id
        }
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # helper method to get the object with given todo id
    def get_object(self, todo_id, user_id):
        try:
            return Todo.objects.get(id=todo_id, user=user_id)
        except Todo.DoesNotExist:
            return None

    # to get a specific todo
    def get(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id, request.user_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exist"},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # to updata a todo
    def put(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id, request.user_id)
        if not todo_instance:
            return Response(
                {"res":"Object with todo id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'isComplete': request.data.get('isComplete'),
            'deadline': request.data.get('deadline'),
            'user': request.user.id
        }
        serializer = TodoSerializer(instance=todo_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # to delete a todo
    def delete(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id, request.user_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exist"},
                status = status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted"},
            status=status.HTTP_200_OK
        )
        