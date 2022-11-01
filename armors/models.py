from django.db import models
from django.core.validators import MinValueValidator
import uuid


class Armor(models.Model):
    class CategoryChoice(models.TextChoices):
        WIZ = "1", "Wizard"
        WAR = "2", "Warrior"
        ARC = "3", "Archer"

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    damage = models.IntegerField(validator=[MinValueValidator(0)])
    category = models.CharField(choices=CategoryChoice.choices)
    inventory = models.ManyToManyField(
        "inventories.Inventory", related_name="armors")
