from django.db import models
import uuid
from categories.models import CategoriesName


class Armor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    defense = models.PositiveIntegerField()
    category = models.CharField(max_length=20, choices=CategoriesName.choices)
    inventory = models.ManyToManyField("inventories.Inventory", related_name="armors")
