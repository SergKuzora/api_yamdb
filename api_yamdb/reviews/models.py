from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Review(models.Model):
    pass


class Comments(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
