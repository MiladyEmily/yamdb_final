from django.core.exceptions import ValidationError
from django.utils import timezone


def year_title(value):
    year = timezone.now().year
    if value > year:
        raise ValidationError(
            f'{value} не может быть больше {year}'
        )
