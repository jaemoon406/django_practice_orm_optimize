from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)


class CustomUser(AbstractUser):
    gender = models.IntegerField(choices=GENDER_CHOICES)

    class Meta:
        db_table = 'user'
