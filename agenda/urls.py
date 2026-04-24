# agenda/urls.py

from django.urls import path
from . import views  # Solo necesitas esta importación de vistas

app_name = 'agenda' 

urlpatterns = [
    # Ruta para la lista (esta ya estaba bien)
    path('', views.TaskList.as_view(), name='task_list'),
    
    # Ruta para crear (corregida)
    # 'new/' está bien, pero 'create/' es más estándar
    path('create/', views.TaskCreate.as_view(), name='task_create'),

    # Ruta para editar (corregida)
    path('edit/<int:pk>/', views.TaskEdit.as_view(), name='task_edit'),

    # Ruta para eliminar (corregida)
    path('delete/<int:pk>/', views.TaskDelete.as_view(), name='task_delete'),
]