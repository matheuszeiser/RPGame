import uuid
from django.db import models

class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=127)
    required_level = models.PositiveIntegerField()
    description = models.TextField()
    
