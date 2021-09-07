from django.contrib.auth import get_user_model
from Django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


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
