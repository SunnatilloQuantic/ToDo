from django.urls import path
from . import views

urlpatterns = [
    path(r'todo/', views.TodoView.as_view(), name='Todo List'),
    path(r'todo/<str:pk>/',views.todoDetail, name='Todo id List'),
    path(r'create/',views.todoCreate, name='Todo create '),
    path(r'update/<str:pk>/',views.todoUpdate, name='Todo update'),
    path(r'delete/', views.todoDelete, name='Todo delete'),
]
