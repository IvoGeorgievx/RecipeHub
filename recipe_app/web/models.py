from django.core.validators import MinLengthValidator
from django.db import models

from recipe_app.auth_app.models import UserProfile
from recipe_app.enums import Enums


class Recipes(models.Model):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(4)], null=False, blank=False)
    recipe_type = models.CharField(max_length=255, choices=Enums.recipe_enum, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.recipe_type}"
