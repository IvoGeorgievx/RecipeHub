from django.contrib.auth.models import User
from django.db import models

from recipe_app.auth_app import validators
from recipe_app.enums import Enums


class UserProfile(models.Model):
    MAX_LENGTH_NAME = 20
    MAX_LENGTH_EMAIL = 50

    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=MAX_LENGTH_NAME,
                                  validators=[validators.validate_name],
                                  null=True,
                                  blank=True)
    last_name = models.CharField(max_length=MAX_LENGTH_NAME,
                                 validators=[validators.validate_name],
                                 null=True,
                                 blank=True)
    email = models.EmailField(max_length=MAX_LENGTH_EMAIL, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    gender = models.CharField(max_length=255, choices=Enums.gender_enum, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
