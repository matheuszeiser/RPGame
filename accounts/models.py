import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
