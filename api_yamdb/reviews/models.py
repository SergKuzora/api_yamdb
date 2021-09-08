from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title


class Title(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    Category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='titles',
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(Genre)

    class Meta:
        ordering = ['-pub_date']
