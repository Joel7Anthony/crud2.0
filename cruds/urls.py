from django.urls import path
from .views import list_crud1

urlpatterns = [
  path('', list_crud1),
  
] 