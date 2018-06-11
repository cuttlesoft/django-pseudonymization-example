from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, UserManager as AuthUserManager

from app.utils import mask, unmask


class UserQuerySet(models.QuerySet):
    pass


class UserManager(AuthUserManager):
    def get_queryset(self):
        return UserQuerySet(self.model)


class User(AbstractUser):

    phone_regex = RegexValidator(
        regex=r'^\+?[1-9]\d{1,14}$',
        message="Phone number must have the format: '+9999999999'.",
    )

    _name = models.CharField(max_length=128, blank=True)
    _phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    _date_of_birth = models.DateField(blank=True, null=True)
    _ip_address = models.GenericIPAddressField(blank=True, null=True)

    @property
    def name(self):
        return unmask(self._name)

    @name.setter
    def name(self, value):
        self._name = mask(value)

    @property
    def phone(self):
        return unmask(self._phone)

    @phone.setter
    def phone(self, value):
        self._phone = mask(value)

    @property
    def date_of_birth(self):
        return unmask(self._date_of_birth)

    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = mask(value)

    @property
    def ip_address(self):
        return unmask(self._ip_address)

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = mask(value)

    objects = UserManager()
