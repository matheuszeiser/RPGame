# Generated by Django 4.1.2 on 2022-11-03 03:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("inventories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Armor",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("defense", models.PositiveIntegerField()),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Warrior", "Warrior"),
                            ("Wizard", "Wizard"),
                            ("Archer", "Archer"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "inventory",
                    models.ManyToManyField(
                        related_name="armors", to="inventories.inventory"
                    ),
                ),
            ],
        ),
    ]
