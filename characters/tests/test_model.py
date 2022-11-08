from django.test import TestCase
from accounts.models import Account
from attributes.models import Attribute
from categories.models import Category
from characters.models import Character
from inventories.models import Inventory
from django.db import IntegrityError 

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
        cls.second_account_data = {
            "username": "kenzinha",
            "password": "1234",
            "email": "kenzinha@mail.com",
            "first_name": "Ken",
            "last_name": "Player",
        }
        cls.account = Account.objects.create(**cls.account_data)
        cls.attributes_tooro = Attribute.objects.create()
        cls.inventory_tooro = Inventory.objects.create()
        cls.category = Category.objects.create(name="Wizard", description="A wizard...")
        cls.tooro_data = {
            "nick_name": "Tooro",
            "category_name": "Wizard",
            "account": cls.account,
            "attributes": cls.attributes_tooro,
            "inventory": cls.inventory_tooro,
            "category": cls.category,
        }
        cls.attributes_singham = Attribute.objects.create()
        cls.inventory_singham = Inventory.objects.create()
        cls.singham_data = {
            "nick_name": "Singham",
            "category_name": "Wizard",
            "account": cls.account,
            "attributes": cls.attributes_singham,
            "inventory": cls.inventory_singham,
            "category": cls.category,
        }
        cls.tooro = Character.objects.create(**cls.tooro_data)

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

        nick_name_received = type(self.tooro.nick_name)
        nick_name_expected = str

        self.assertTrue(
            nick_name_received == nick_name_expected,
            msg="Verify if the nick_name is a string",
        )

        level_received = type(self.tooro.level)
        level_expected = int

        self.assertTrue(
            level_received == level_expected, msg="Verify if the level is a integer"
        )
        self.assertTrue(
            self.tooro.level > 0,
            msg="Verify if the level is a integer greater than zero",
        )

        health_received = type(self.tooro.health)
        health_expected = int

        self.assertTrue(
            health_received == health_expected, msg="Verify if the health is a integer"
        )
        self.assertTrue(
            self.tooro.level > 0,
            msg="Verify if the health is a integer greater than zero",
        )

        category_name_received = type(self.tooro.category_name)
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

    def test_if_an_account_can_have_multiple_characters(self):
        singham = Character.objects.create(**self.singham_data)

        self.assertEquals(
                2, 
                self.account.characters.count()
            )
        self.assertIs(singham.account, self.account)
        self.assertIs(self.tooro.account, self.account)

    def test_if_character_cannot_belong_to_more_than_one_account(self):           
        second_account = Account.objects.create(**self.second_account_data)

        self.tooro.account = second_account
        self.tooro.save()

        self.assertNotIn(self.tooro, self.account.characters.all()) 
        self.assertIn(self.tooro, second_account.characters.all())

    def test_if_the_character_can_have_a_inventory(self):
        self.assertIs(self.tooro.inventory, self.inventory_tooro)
        self.assertIs(self.tooro, self.inventory_tooro.character)

    def test_if_raise_error_when_inventory_already_have_an_character(self):
        with self.assertRaises(IntegrityError):
            singham = Character.objects.create(**self.singham_data)
            singham.inventory = self.inventory_tooro
            singham.save()

    def test_if_an_category_can_have_multiple_characters(self):
        singham = Character.objects.create(**self.singham_data)

        self.assertEquals(
                2, 
                self.category.characters.count()
            )
        self.assertIs(singham.category, self.category)
        self.assertIs(self.tooro.category, self.category)

    def test_if_character_cannot_belong_to_more_than_one_category(self):           
        second_category = Category.objects.create(name="Warrior", description="A warrior...")

        self.tooro.category = second_category
        self.tooro.save()

        self.assertNotIn(self.tooro, self.category.characters.all()) 
        self.assertIn(self.tooro, second_category.characters.all())

    def test_if_the_character_can_have_attributes(self):
        self.assertIs(self.tooro.attributes, self.attributes_tooro)
        self.assertIs(self.tooro, self.attributes_tooro.character)

    def test_if_raise_error_when_attributes_already_have_an_character(self):
        with self.assertRaises(IntegrityError):
            singham = Character.objects.create(**self.singham_data)
            singham.attributes = self.attributes_tooro
            singham.save()
