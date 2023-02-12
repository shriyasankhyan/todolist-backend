# from rest_framework import routers
# from .views import *

# router=routers.DefaultRouter()
# router.register(r'api/todos',TodoViewSet,'todos')
from django.urls import path, include
from .views import (
    TodoListApiView,
    TodoDetailApiView
)

urlpatterns = [
    path('api/todos', TodoListApiView.as_view()),
    path('api/todos/<int:todo_id>/', TodoDetailApiView.as_view()),
]