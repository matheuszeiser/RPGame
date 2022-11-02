# Generated by Django 4.1.2 on 2022-11-01 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('inventories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attributes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nick_name', models.CharField(max_length=50, unique=True)),
                ('level', models.PositiveIntegerField(default=1)),
                ('health', models.PositiveIntegerField(default=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to=settings.AUTH_USER_MODEL)),
                ('atributes', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='character', to='attributes.attribute')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='categories.category')),
                ('inventory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='character', to='inventories.inventory')),
            ],
        ),
    ]