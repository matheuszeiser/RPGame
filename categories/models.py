from django.db import models
import uuid


class Name(models.TextChoices):
    WARRIOR = "Warrior"
    WIZARD = "Wizard"
    ARCHER = "Archer"


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=15, choices=Name.choices)
    description = models.TextField()
    skills = models.ManyToManyField(
        "skills.Skill",
        on_delete=models.CASCADE,
        related_name="categories",
    )
