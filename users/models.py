from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    phone_regex = RegexValidator(
        regex=r'^\+?[1-9]\d{1,14}$',
        message="Phone number must have the format: '+9999999999'.",
    )

    name = models.CharField(max_length=128, blank=True)
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
