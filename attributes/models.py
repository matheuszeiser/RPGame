import uuid
from django.db import models


class Attribute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    strength = models.PositiveIntegerField(default=1)
    agility = models.PositiveIntegerField(default=1)
    intelligence = models.PositiveIntegerField(default=1)
    endurance = models.PositiveIntegerField(default=1)
