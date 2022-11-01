from django.db import models
from django.utils import timezone

import uuid


class Character(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nick_name = models.CharField(max_length=50, unique=True)
    level = models.PositiveIntegerField(default=1, max_digits=2)
    health = models.PositiveIntegerField(default=100, max_digits=3)
    created_at = models.DateTimeField(default=timezone.now)

    account = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="characters"
    )
    inventory = models.OneToOneField(
        "inventories.Inventory", on_delete=models.CASCADE, related_name="character"
    )
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="characters"
    )
    atributes = models.OneToOneField(
        "attributes.Attribute", on_delete=models.CASCADE, related_name="character"
    )
