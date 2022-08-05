from django.urls import path
from .views import list_crud1, create_task, delete_task 

urlpatterns = [
  path('', list_crud1),
  path('new/', create_task, name='create_task'),
  path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
]