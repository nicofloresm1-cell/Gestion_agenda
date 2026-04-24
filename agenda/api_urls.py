from django.urls import path
from .views_api import TaskListCreateAPI, TaskDetailAPI

urlpatterns = [
    path('tasks/', TaskListCreateAPI.as_view(), name='api_task_list'),
    path('tasks/<int:pk>/', TaskDetailAPI.as_view(), name='api_task_detail'),
]
