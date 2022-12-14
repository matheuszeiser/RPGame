# Generated by Django 4.1.2 on 2022-11-03 03:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attribute",
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
                (
                    "strength",
                    models.PositiveIntegerField(blank=True, default=1, null=True),
                ),
                (
                    "agility",
                    models.PositiveIntegerField(blank=True, default=1, null=True),
                ),
                (
                    "intelligence",
                    models.PositiveIntegerField(blank=True, default=1, null=True),
                ),
                (
                    "endurance",
                    models.PositiveIntegerField(blank=True, default=1, null=True),
                ),
            ],
        ),
    ]
