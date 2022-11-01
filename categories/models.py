from django.db import models


class Name(models.TextChoices):
    WARRIOR = "Warrior"
    WIZARD = "Wizard"
    ARCHER = "Archer"


class Category(models.Model):
    name = models.CharField(max_length=15, choices=Name.choices)
    description = models.TextField()
    skills = models.ManyToManyField(
        "skills.Skill",
        on_delete=models.CASCADE,
        related_name="categories",
    )
