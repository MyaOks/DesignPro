from django.contrib.auth.models import AbstractUser
from django.db import models

class AdvUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('user', 'Пользователь'),
        ('guest', 'Гость')
    ]
    first_name = models.CharField(max_length=254, verbose_name='Имя', blank=False, default='')
    last_name = models.CharField(max_length=254, verbose_name='Фамилия', blank=False, default='')
    patronymic = models.CharField(max_length=254, verbose_name='Отчество', blank=True)
    username = models.CharField(max_length=254, verbose_name='Логин', unique=True, blank=False, default='')
    email = models.CharField(max_length=254, verbose_name='Почта', unique=True, blank=False, default='')
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=False, default='')
    role = models.CharField(max_length=254, verbose_name='Роль', choices=ROLE_CHOICES, default='user')

    USERNAME_FIELD = 'username'


