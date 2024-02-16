from django.db import models
from utils.models import BaseModel


class OptionType(models.TextChoices):
    BUTTON = "Button"
    SELECT = "Select"
    TEXT = "Text"
    NUMBER = "Number"
    MULTIPLE_CHOICE = "Multiple choice"


class Option(BaseModel):
    title = models.CharField(max_length=64)
    type = models.CharField(max_length=64, choices=OptionType.choices)

    def __str__(self):
        return self.title



