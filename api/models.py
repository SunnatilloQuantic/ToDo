from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    color = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title