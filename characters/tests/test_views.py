from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from accounts.models import Account
from categories.models import Category
from characters.models import Character


class CharacterViewTests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/char/"

        cls.admin_user = Account.objects.create_superuser(
            username="admin",
            password="1234",
            email="admin@email.com",
            first_name="admin",
            last_name="admin",
        )

        cls.common_user = Account.objects.create_user(
            username="deb",
            password="1234",
            email="debora@email.com",
            first_name="Débora",
            last_name="Corrêa",
        )

        cls.common_user_token, _ = Token.objects.get_or_create(user=cls.common_user)

        cls.admin_token, _ = Token.objects.get_or_create(user=cls.admin_user)

        Category.objects.create(
            name="Warrior", description="A warrior is a category of..."
        )

        cls.character_data = {"nick_name": "test", "category_name": "Warrior"}

        cls.admin_character_data = {
            "nick_name": "adminchar",
            "category_name": "Warrior",
        }

    def test_authenticated_user_can_create_character(self):
        """
        Verifica se o usuário autenticado pode criar um personagem com dados corretos
        """
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.common_user_token.key}"
        )

        response = self.client.post(self.BASE_URL, self.character_data)

        self.assertEqual(response.status_code, 201)

        self.assertEqual(Character.objects.count(), 1)

    def test_unauthenticated_user_can_not_create_character(self):
        """
        Verifica se usuário não autenticado não pode criar um personagem
        """
        response = self.client.post(self.BASE_URL, self.character_data)

        self.assertEqual(response.status_code, 401)

        self.assertEqual(
            response.data, {"detail": "Authentication credentials were not provided."}
        )

    def test_create_character_missing_keys(self):
        """
        Verifica se a requisição retorna erro com chaves faltando no body
        """
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.common_user_token.key}"
        )

        response = self.client.post(self.BASE_URL, {})

        self.assertEqual(response.status_code, 400)

        self.assertEqual(
            response.data,
            {
                "nick_name": ["This field is required."],
                "category_name": ["This field is required."],
            },
        )

        self.assertEqual(Character.objects.count(), 0)

    def test_returning_keys(self):
        """
        Verifica se o retorno da requisição tem as chaves esperadas
        """
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.common_user_token.key}"
        )

        response = self.client.post(self.BASE_URL, self.character_data)

        expected_keys = {
            "id",
            "category",
            "account",
            "attributes",
            "nick_name",
            "level",
            "health",
            "created_at",
            "inventory",
        }

        self.assertSetEqual(set(response.data.keys()), expected_keys)

    def test_user_can_list_their_characters(self):
        """
        Verifica se usuário autenticado pode listar apenas seus personagens
        """
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.admin_token.key}")

        self.client.post(self.BASE_URL, self.admin_character_data)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.common_user_token.key}"
        )

        character = self.client.post(self.BASE_URL, self.character_data)

        response = self.client.get(self.BASE_URL)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data[0], character.data)

        self.assertEqual(len(response.data), 1)

    def test_unauthenticated_user_can_not_list_characters(self):
        """
        Verifica se usuário não autenticado não pode listar personagens
        """
        response = self.client.get(self.BASE_URL)

        self.assertEqual(response.status_code, 401)

        self.assertEqual(
            response.data, {"detail": "Authentication credentials were not provided."}
        )

    def test_authenticated_user_can_retrieve_their_character(self):
        """
        Verifica se usuário autenticado pode listar seu personagem pelo id
        """
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.common_user_token.key}"
        )

        character = self.client.post(self.BASE_URL, self.character_data)

        response = self.client.get(f"{self.BASE_URL}{character.data['id']}/")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data["id"], character.data["id"])

    def test_common_user_can_not_retrieve_other_user_character(self):
        """
        Verifica se o usuário não dono do personagem não consegue listá-lo pelo id
        """
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.admin_token.key}")

        character = self.client.post(self.BASE_URL, self.admin_character_data)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.common_user_token.key}"
        )

        response = self.client.get(f"{self.BASE_URL}{character.data['id']}/")

        self.assertEqual(response.status_code, 403)

        self.assertEqual(
            response.data,
            {"detail": "You do not have permission to perform this action."},
        )

    def test_unauthenticated_user_can_not_retrieve_character(self):
        """
        Verifica se usuário não autenticado não pode listar personagem pelo id
        """
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.admin_token.key}")

        character = self.client.post(self.BASE_URL, self.admin_character_data)

        self.client.credentials(HTTP_AUTHORIZATION="")

        response = self.client.get(f"{self.BASE_URL}{character.data['id']}/")

        self.assertEqual(response.status_code, 401)

        self.assertEqual(
            response.data,
            {"detail": "Authentication credentials were not provided."},
        )

    def test_admin_can_retrieve_any_character(self):
        """
        Verifica se o usuário administrador pode listar qualquer personagem pelo id
        """
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.common_user_token.key}"
        )

        character = self.client.post(self.BASE_URL, self.character_data)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.admin_token.key}")

        response = self.client.get(f"{self.BASE_URL}{character.data['id']}/")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data["id"], character.data["id"])

    def test_user_can_update_their_character(self):
        """
        Verifica se o usuário pode atualizar seu personagem
        """
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.common_user_token.key}"
        )

        character = self.client.post(self.BASE_URL, self.character_data)

        response = self.client.patch(
            f"{self.BASE_URL}{character.data['id']}/", {"nick_name": "updatedChar"}
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data["nick_name"], "updatedChar")

    def test_common_user_can_not_update_other_user_character(self):
        """
        Verifica se usuário comum não pode atualizar o personagem que não é seu
        """
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.admin_token.key}")

        character = self.client.post(self.BASE_URL, self.admin_character_data)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.common_user_token.key}"
        )

        response = self.client.patch(
            f"{self.BASE_URL}{character.data['id']}/", {"nick_name": "updatedChar"}
        )

        self.assertEqual(response.status_code, 403)

        self.assertEqual(
            response.data,
            {"detail": "You do not have permission to perform this action."},
        )

    def test_admin_can_update_any_character(self):
        """
        Verifica se o usuário administrador pode atualizar qualquer personagem
        """
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.common_user_token.key}"
        )

        character = self.client.post(self.BASE_URL, self.character_data)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.admin_token.key}")

        response = self.client.patch(
            f"{self.BASE_URL}{character.data['id']}/", {"nick_name": "updatedChar"}
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data["nick_name"], "updatedChar")

    def test_user_can_delete_their_character(self):
        """
        Verifica se o usuário pode deletar seu personagem
        """
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.common_user_token.key}"
        )

        character = self.client.post(self.BASE_URL, self.character_data)

        response = self.client.delete(f"{self.BASE_URL}{character.data['id']}/")

        self.assertEqual(response.status_code, 204)

    def test_common_user_can_not_delete_other_user_character(self):
        """
        Verifica se usuário comum não pode deletar o personagem que não é seu
        """
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.admin_token.key}")

        character = self.client.post(self.BASE_URL, self.admin_character_data)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.common_user_token.key}"
        )

        response = self.client.delete(f"{self.BASE_URL}{character.data['id']}/")

        self.assertEqual(response.status_code, 403)

        self.assertEqual(
            response.data,
            {"detail": "You do not have permission to perform this action."},
        )

    def test_admin_can_delete_any_character(self):
        """
        Verifica se o usuário administrador pode deletar qualquer personagem
        """
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {self.common_user_token.key}"
        )

        character = self.client.post(self.BASE_URL, self.character_data)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.admin_token.key}")

        response = self.client.delete(f"{self.BASE_URL}{character.data['id']}/")

        self.assertEqual(response.status_code, 204)
