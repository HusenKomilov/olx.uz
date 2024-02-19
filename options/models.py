from django.db import models
from utils.models import BaseModel
from options.choices import OptionType


class Option(BaseModel):  # Количество комнат, Этаж, Ремонт, Меблирована
    title = models.CharField(max_length=64)
    option_type = models.CharField(max_length=64, choices=OptionType.choices)
    order = models.IntegerField(default=0)
    placeholder = models.CharField(max_length=64, blank=True, null=True)
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class OptionValue(BaseModel):  # Все объявления, Авторский проект, Евроремонт
    title = models.CharField(max_length=128)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name="option")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title
