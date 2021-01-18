from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^todo/', views.todoList, name='Todo list'),
    url(r'^todo/<str:pk>/',views.todoDetail, name='Todo id get'),
    url(r'^create/',views.todoCreate, name='Todo create '),
    url(r'^update/<str:pk>/',views.todoUpdate, name='Todo update'),
    url(r'^delete/', views.todoDelete, name='Todo delete'),
]
