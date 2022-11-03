from django.db import models
import uuid


class CategoriesName(models.TextChoices):
    WARRIOR = "Warrior"
    WIZARD = "Wizard"
    ARCHER = "Archer"


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=15, choices=CategoriesName.choices)
    description = models.TextField()
    skills = models.ManyToManyField("skills.Skill", related_name="categories")
