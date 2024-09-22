# Generated by Django 5.1.1 on 2024-09-16 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("form", "0002_remove_register_firstname_remove_register_lastname_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="hostel",
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
                ("hostelName", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("manager", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=10)),
                ("rooms", models.IntegerField()),
            ],
        ),
    ]