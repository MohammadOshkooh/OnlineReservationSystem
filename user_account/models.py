from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    fields: username, password, first_name, last_name, email, address, phone_number
    """
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
