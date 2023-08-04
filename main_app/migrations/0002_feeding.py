# Generated by Django 4.2.3 on 2023-08-03 00:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feeding",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "water_needs",
                    models.CharField(
                        choices=[
                            ("I", "infrequent"),
                            ("R", "regular"),
                            ("F", "frequent"),
                        ],
                        default="I",
                        max_length=1,
                        verbose_name="Watering Needs",
                    ),
                ),
            ],
        ),
    ]