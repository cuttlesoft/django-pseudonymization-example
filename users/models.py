from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

from app.fields import PseudonymizedField
from app.utils import mask, unmask


class User(AbstractUser):

    phone_regex = RegexValidator(
        regex=r'^\+?[1-9]\d{1,14}$',
        message="Phone number must have the format: '+9999999999'.",
    )

    name = PseudonymizedField(
        models.CharField, (mask, unmask), max_length=128, blank=True
    )
    phone = PseudonymizedField(
        models.CharField,
        (mask, unmask),
        validators=[phone_regex],
        max_length=16,
        blank=True,
    )
    date_of_birth = PseudonymizedField(
        models.DateField, (mask, unmask), blank=True, null=True
    )
    ip_address = PseudonymizedField(
        models.GenericIPAddressField, (mask, unmask), blank=True, null=True
    )
