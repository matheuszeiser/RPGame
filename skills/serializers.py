from rest_framework import serializers

from categories.models import Category

from .models import Skill
import ipdb


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill

        fields = [
            "id",
            "name",
            "required_level",
            "description"
        ]


class ListSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'skills'
        ]
        depth = 2


class ListSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = [
            "id",
            'name',
            "required_level",
            "description",
        ]
