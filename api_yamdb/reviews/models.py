from random import choice

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .utils import Util

CHOICES = (
    ('user', 'user'),
    ('admin', 'admin'),
    ('moderator', 'moderator')
)


def validate_username_me(value):
    if value == 'me':
        raise ValidationError(
            ('Username can`t be "me"'),
            params={'value': value},
        )


class User(AbstractUser):
    username = models.CharField(validators=(validate_username_me,),
                                max_length=50, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(max_length=16, choices=CHOICES,
                            default='user', blank=True)
    confirmation_code = models.IntegerField(default=0)

    @property
    def is_user(self):
        return self.role == 'user'
    
    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'


@receiver(post_save, sender=User)
def post_save(sender, instance, created, **kwargs):
    if created:
        confirmation_code = choice(range(1000, 10000))
        instance.confirmation_code = confirmation_code
        instance.save()

        email_body = (f'Hi, {instance.username}. '
                      f'We have delivered confirmation code'
                      f' to you!\nYour code is: {confirmation_code}')
        data = {'email_body': email_body,
                'to_email': instance.email,
                'email_subject': 'That`s your code!'}

        Util.send_email(data)


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        related_name='titles',
        on_delete=models.SET_NULL,
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        blank=True
    )

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.text


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    text = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)])
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return self.text


class Comments(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
