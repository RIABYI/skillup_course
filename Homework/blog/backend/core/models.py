from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    """Base post model."""

    title = models.CharField(max_length=100)
    body = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")