# Generated by Django 4.2.4 on 2023-09-14 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travelapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="emp",
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
                ("name", models.CharField(max_length=240)),
                ("post", models.CharField(max_length=240)),
                ("about", models.TextField()),
                ("dp", models.ImageField(upload_to="dp")),
            ],
        ),
    ]
