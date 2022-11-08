from django.test import TestCase

from accounts.models import Account
from attributes.models import Attribute
from categories.models import Category
from characters.models import Character
from inventories.models import Inventory


class CharacterModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.account_data = {
            "username": "kenzinho",
            "password": "1234",
            "email": "kenzinho@mail.com",
            "first_name": "Ken",
            "last_name": "Player",
        }
        cls.account = Account.objects.create(**cls.account_data)
        cls.attributes = Attribute.objects.create()
        cls.inventory = Inventory.objects.create()
        cls.category = Category.objects.create(name="Wizard", description="A wizard...")
        cls.character_data = {
            "nick_name": "Tooro",
            "category_name": "Wizard",
            "account": cls.account,
            "attributes": cls.attributes,
            "inventory": cls.inventory,
            "category": cls.category,
        }
        cls.character = Character.objects.create(**cls.character_data)

    def test_nick_name_max_length(self):

        expected_max_length = 50
        result_max_length = Character._meta.get_field("nick_name").max_length
        msg = f"Verify if property `max_length` from nick_name is defined as {expected_max_length}"
        self.assertEqual(expected_max_length, result_max_length, msg)

    def test_category_name_max_length(self):

        expected_max_length = 20
        result_max_length = Character._meta.get_field("category_name").max_length
        msg = f"Verify if property `max_length` from category_name is defined as {expected_max_length}"
        self.assertEqual(expected_max_length, result_max_length, msg)

    def test_attributes_data_type(self):

        nick_name_received = type(self.character.nick_name)
        nick_name_expected = str

        self.assertTrue(
            nick_name_received == nick_name_expected,
            msg="Verify if the nick_name is a string",
        )

        level_received = type(self.character.level)
        level_expected = int

        self.assertTrue(
            level_received == level_expected, msg="Verify if the level is a integer"
        )
        self.assertTrue(
            self.character.level > 0,
            msg="Verify if the level is a integer greater than zero",
        )

        health_received = type(self.character.health)
        health_expected = int

        self.assertTrue(
            health_received == health_expected, msg="Verify if the health is a integer"
        )
        self.assertTrue(
            self.character.level > 0,
            msg="Verify if the health is a integer greater than zero",
        )

        category_name_received = type(self.character.category_name)
        category_name_expected = str

        self.assertTrue(
            category_name_received == category_name_expected,
            msg="Verify if the category_name is a string",
        )

    def test_if_nick_name_unique(self):
        unique = Character._meta.get_field("nick_name").unique

        self.assertTrue(unique)

    def test_if_nick_name_cannot_be_null(self):
        nullable = Character._meta.get_field("nick_name").null

        self.assertFalse(nullable)
