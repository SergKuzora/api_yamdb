from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from random import choice
from .utils import Util


CHOICES = (
    ('user', 'user'),
    ('admin', 'admin'),
    ('moderator', 'moderator')
)

class User(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    bio = models.TextField(
        'Биография',
        blank=True,
    ) 
    role = models.CharField(max_length=16, choices=CHOICES, default='user', blank=True)
    confirmation_code = models.CharField(max_length=4, blank=True)

@receiver(post_save, sender=User)
def post_save(sender, instance, created, **kwargs):
    if created:
        confirmation_code = choice(range(1000, 10000))
        instance.confirmation_code = confirmation_code
        instance.save()

        email_body = (f'Hi, {instance.username}. We have delivered confirmation code'
                      f' to you!\nYour code is: {confirmation_code}')
        data={'email_body': email_body,
              'to_email': instance.email,
              'email_subject': f'That`s your code!'}

        Util.send_email(data)