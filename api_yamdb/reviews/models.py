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
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Title(models.Model):
    text = models.CharField(max_length=200)
    Category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        related_name='category'
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='genre'
    )

    class Meta:
        ordering = ['-text']
    
    def __str__(self):
        return self.text
