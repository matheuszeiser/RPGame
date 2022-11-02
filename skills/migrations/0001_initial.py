# Generated by Django 4.1.2 on 2022-11-01 18:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=127)),
                ('required_level', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]