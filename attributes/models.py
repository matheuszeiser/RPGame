import uuid
from django.db import models

class Attribute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    strength = models.PositiveIntegerField()
    agility = models.PositiveIntegerField()
    intelligence = models.PositiveIntegerField()
    endurance = models.PositiveIntegerField()
    
