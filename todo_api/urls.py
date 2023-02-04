from django.urls import path
from .views import TaskCreateView

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='task-create'),
]