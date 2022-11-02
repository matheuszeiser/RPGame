# Generated by Django 4.1.2 on 2022-11-01 18:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('Warrior', 'Warrior'), ('Wizard', 'Wizard'), ('Archer', 'Archer')], max_length=15)),
                ('description', models.TextField()),
                ('skills', models.ManyToManyField(related_name='categories', to='skills.skill')),
            ],
        ),
    ]