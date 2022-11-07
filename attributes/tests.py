from django.test import TestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from accounts.models import Account
from attributes.models import Attribute
from categories.models import Category
from characters.models import Character


class AttributeModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:   
        cls.warrior = Attribute.objects.create(
            **{
                "strength": 5,
                "agility": 1,
                "intelligence": 1,
                "endurance": 2,
            }
        )

    def test_attributes_data_type(self):

        # Tests and validates the input types

        warrior = Attribute.objects.get(id=self.warrior.id)
        strength_type_received = type(warrior.strength)
        strength_type_expected = int

        strength_lvl = warrior.strength

        self.assertTrue(strength_type_received == strength_type_expected, msg="Verify if the strength is a integer")
        self.assertTrue(strength_lvl > 0, msg="Verify if the strength is a integer greater than zero")

        agility_type_received = type(warrior.agility)
        agility_type_expected = int

        agility_lvl = warrior.agility

        self.assertTrue(agility_type_received == agility_type_expected, msg="Verify if the agility is a integer")
        self.assertTrue(agility_lvl > 0, msg="Verify if the agility is a integer greater than zero")

        intelligence_type_received = type(warrior.strength)
        intelligence_type_expected = int

        intelligence_lvl = warrior.intelligence

        self.assertTrue(intelligence_type_received == intelligence_type_expected, msg="Verify if the intelligence is a integer")
        self.assertTrue(intelligence_lvl > 0, msg="Verify if the intelligence is a integer greater than zero")


class AttributeViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user1 = Account.objects.create_superuser(
            **{
                "username": "silv",
                "password": "abcd",
                "first_name": "Gab",
                "last_name": "Silv",
                "email": "gab@mail.com",
                "is_superuser": True
            }
        )

        cls.category_data = {
                "name": "Warrior",
                "description": "The prince of the Saiyans"
            }
    

        cls.char_user1_data = {            
                "nick_name": "Vegeta",
                "category_name": "Warrior"
            }

        cls.char_user1_data = {            
                "nick_name": "Vegeta",
                "category_name": "Warrior"
            }

        cls.char_user1_update = {
            "agility": 4
        }

        cls.token_user1 = Token.objects.create(user=cls.user1)

    def test_attributes_update(self):

        #Tests the cration of a new category by an admin

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token_user1.key}")
        category_response = self.client.post("/api/admin/categories/", self.category_data)
        create_category_expected_status = status.HTTP_201_CREATED
        create_category_received_status = category_response.status_code
        category_msg = "Verify the body request and all the input types given"
        self.assertEqual(create_category_expected_status, create_category_received_status, category_msg)

        #Tests the creation of a characte by a user

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token_user1.key}")
        char_response = self.client.post("/api/char/", self.char_user1_data)
        create_char_expected_status = status.HTTP_201_CREATED
        create_char_received_status = char_response.status_code
        char_msg = "Verify if the category_name is a valid choice"
        self.assertEqual(create_char_expected_status, create_char_received_status, char_msg)

        #Tests character attributes update

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token_user1.key}")
        char = Character.objects.get(nick_name="Vegeta")
        response = self.client.patch(f"/api/char/{char.id}/attributes/", self.char_user1_update)
        update_char_expected_status = status.HTTP_200_OK
        received_status = response.status_code
        expected_agility = self.char_user1_update["agility"]
        char_updated = Character.objects.get(nick_name="Vegeta")
        self.assertEqual(update_char_expected_status, received_status, msg = "Verify authorization and id provided")
        self.assertEqual(expected_agility, char_updated.attributes.agility)


        