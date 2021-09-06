from django.contrib.auth import get_user_model
from Django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Review(models.Model):
    text = models.CharField(max_length=200)
    score = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)])


class Comments(models.Model):
    text = models.CharField(max_length=200)
