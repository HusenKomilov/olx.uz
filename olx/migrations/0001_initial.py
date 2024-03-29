# Generated by Django 4.2.7 on 2024-02-19 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("options", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("update_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
                ("image", models.ImageField(upload_to="categories")),
                ("order", models.IntegerField(default=0)),
                (
                    "option",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category_options",
                        to="options.option",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="children", to="olx.category"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="District",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("update_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("update_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SubCategories",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("update_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="categories", to="olx.category"
                    ),
                ),
                (
                    "option",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subcategory_option",
                        to="options.option",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="olx.subcategories"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Posts",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("update_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
                ("content", models.TextField()),
                ("watched", models.IntegerField(default=0, editable=False)),
                ("price", models.IntegerField(blank=True, null=True)),
                (
                    "price_type",
                    models.CharField(
                        choices=[("Naxt", "Price"), ("Tekin", "Free"), ("Obmen", "Exchange")], max_length=64
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Aktiv", "Active"),
                            ("Faol emas", "Inactive"),
                            ("Jarayonda", "Process"),
                            ("To'lanmagan", "Not Payed"),
                        ],
                        max_length=64,
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("phone", phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ("is_shutdown", models.BooleanField(default=False)),
                ("is_agreement", models.BooleanField(default=False)),
                (
                    "district",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="districts", to="olx.district"
                    ),
                ),
                (
                    "subcategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="subcategory", to="olx.subcategories"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="author", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="district",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="regions", to="olx.region"
            ),
        ),
    ]
