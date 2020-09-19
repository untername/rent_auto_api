from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as lazy
from .managers import CustomUserManager
from django.utils import timezone
from typing import List, Any, Tuple


LANGS: List[Tuple[str, str]] = [
    ('en', 'English'),
    ('ru', 'Russian'),
]


class UpdatedUser(AbstractUser):

    """ Переопределенный класс юзера, для авторизации по паре email/password, вместо логина. """

    username = None
    email = models.EmailField(lazy('email address'), unique=True)
    name = models.TextField()

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: List[Any] = []
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email


class Renter(models.Model):

    """ Класс для арендатора автомобиля. """

    name = models.CharField(max_length=100)
    email = models.EmailField()
    language = models.CharField(max_length=40, choices=LANGS)

    def __str__(self) -> str:
        return self.email


class Auto(models.Model):

    """ Класс для авто, имеет отношение типа 'Многие ко многим'."""

    drivers = models.ManyToManyField(Renter, related_name='cars')
    auto_name = models.CharField(max_length=90)
    year = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.auto_name
