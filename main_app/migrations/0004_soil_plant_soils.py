# Generated by Django 4.2.3 on 2023-08-03 23:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0003_feeding_plant"),
    ]

    operations = [
        migrations.CreateModel(
            name="Soil",
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
                ("soil_type", models.CharField(max_length=50)),
                ("benefit", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="plant",
            name="soils",
            field=models.ManyToManyField(to="main_app.soil"),
        ),
    ]
