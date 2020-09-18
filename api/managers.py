from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as lazy
from typing import Union, Any, Type


class CustomUserManager(BaseUserManager):

    """ Менеджер для переопределенной модели юзера. """

    def create_user(self, email: str, password: str, **kwargs: Union[str, Any]) -> Type[BaseUserManager]:
        if not email:
            raise ValueError(lazy('Please, input email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email: str, password: str, **params: Union[str, Any]) -> Type[BaseUserManager]:
        params.setdefault('is_staff', True)
        params.setdefault('is_superuser', True)
        params.setdefault('is_active', True)

        if params.get('is_staff') is not True:
            raise ValueError(lazy('superuser must have a is_staff=True'))
        if params.get('is_superuser') is not True:
            raise ValueError(lazy('superuser must have a is_superuser=True'))

        return self.create_user(email, password, **params)
