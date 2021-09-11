from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from random import choice
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
