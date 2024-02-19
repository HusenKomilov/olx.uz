from django.db import models


class PriceTypeChoices(models.TextChoices):
    PRICE = "Naxt"
    FREE = "Tekin"
    EXCHANGE = "Obmen"


class StatusChoices(models.TextChoices):
    ACTIVE = "Aktiv"
    INACTIVE = "Faol emas"
    PROCESS = "Jarayonda"
    NOT_PAYED = "To'lanmagan"


class CodeChoice(models.TextChoices):
    TOP = "TOP"
    TOP_UP = "Tepaga chiqarish"
    VIP = "VIP"


class PlanChoiceDetail(models.TextChoices):
    NUll = "Null"
    WEEK = "7 kun"
    MONTH = "30 kun"
