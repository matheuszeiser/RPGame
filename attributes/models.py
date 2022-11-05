import uuid
from django.db import models


class Attribute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    strength = models.PositiveIntegerField(default=1, null=True, blank=True)
    agility = models.PositiveIntegerField(default=1, null=True, blank=True)
    intelligence = models.PositiveIntegerField(default=1, null=True, blank=True)
    endurance = models.PositiveIntegerField(default=1, null=True, blank=True)
