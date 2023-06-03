"""This file contains a custom User model"""
from django.contrib.auth.models import AbstractUser
# --------------------------------------------------------------------------


class User(AbstractUser):
    """A custom User model"""
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f'User({self.username}, {self.email})'
