from django.db import models
from django.utils import timezone

import uuid
from categories.models import CategoriesName


class Character(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nick_name = models.CharField(max_length=50, unique=True)
    level = models.PositiveIntegerField(default=1)
    health = models.PositiveIntegerField(default=100)
    created_at = models.DateTimeField(default=timezone.now)
    category_name = models.CharField(max_length=20, choices=CategoriesName.choices)

    account = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="characters"
    )
    inventory = models.OneToOneField(
        "inventories.Inventory", on_delete=models.CASCADE, related_name="character"
    )
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="characters"
    )
    attributes = models.OneToOneField(
        "attributes.Attribute", on_delete=models.CASCADE, related_name="character"
    )
