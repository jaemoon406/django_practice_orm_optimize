from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, UserManager

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)


class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=15, unique=True)
    username = models.CharField(max_length=30, unique=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=2)
    email = models.EmailField()
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()

    USERNAME_FIELD = 'username'
    objects = UserManager()

    class Meta:
        db_table = 'user'
