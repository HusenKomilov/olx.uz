from django.db import models


class OptionType(models.TextChoices):
    BUTTON = "Button"
    SELECT = "Select"
    TEXT = "Text"
    NUMBER = "Number"
    MULTIPLE_CHOICE = "Multiple choice"
