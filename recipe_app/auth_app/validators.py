from django.core.exceptions import ValidationError


def validate_name(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Names must contain only alphabetic characters.")