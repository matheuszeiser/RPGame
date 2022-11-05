# Generated by Django 4.1.2 on 2022-11-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("characters", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="category_name",
            field=models.CharField(
                choices=[
                    ("Warrior", "Warrior"),
                    ("Wizard", "Wizard"),
                    ("Archer", "Archer"),
                ],
                max_length=20,
            ),
        ),
    ]
