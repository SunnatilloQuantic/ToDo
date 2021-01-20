from django.urls import path
from .views import TestView, RegisterView

urlpatterns = [
    path(r'post/', TestView.as_view(), name = "Test View"),
    path(r'register/', RegisterView.as_view(), name = 'Register'),
]