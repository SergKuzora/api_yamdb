from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Users(models.Model):
    username = models.CharField(max_lenght=150)
    email = models.EmailField(max_lenght=254)
    first_name = models.CharField(max_lenght=150)
    last_name = models.CharField(max_lenght=150)
    bio = models.CharField()
    roles = ['user', 'moderator', 'admin']
    role = models.CharField(choices=roles, default='user',)


class Review(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)])
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text


class Comments(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text
