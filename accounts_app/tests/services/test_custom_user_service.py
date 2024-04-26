import unittest

from django.db.transaction import TransactionManagementError
from django.test import TestCase

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, transaction
from psycopg.errors import UniqueViolation

from accounts_app.models import CustomUser
from services.generic.accounts_app.custom_user_service import CustomUserService


class TestCustomUserService(TestCase):
    def setUp(self):
        # Create a user for testing purposes
        self.existing_user, created = CustomUser.objects.get_or_create(first_name='John',
                                                                       last_name='Doe',
                                                                       username='John Doe',
                                                                       email='random@gmail.com',
                                                                       password='random_password')

    def tearDown(self) -> None:
        CustomUser.objects.filter(email__startswith='test_user').delete()

    def test_create_custom_user_should_add_new_user_with_correct_data(self):
        first_name = 'joey'
        last_name = 'dias'
        username = 'joey dias'
        email = 'test_user_1@gmail.com'
        password = 'dias123'

        user = CustomUserService.create_custom_user(first_name=first_name,
                                                    last_name=last_name,
                                                    username=username,
                                                    email=email,
                                                    password=password,
                                                    commit=True)

        self.assertIsInstance(user, CustomUser)
        self.assertEqual(first_name, user.first_name)
        self.assertEqual(last_name, user.last_name)
        self.assertEqual(username, user.username)
        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(password))

    def test_create_custom_user_should_add_new_user_when_commit_is_true(self):
        # Arrange
        first_name = 'joey'
        last_name = 'dias'
        username = 'joey dias'
        email = 'test_user_1@gmail.com'
        password = 'dias123'

        # Act
        user = CustomUserService.create_custom_user(first_name=first_name,
                                                    last_name=last_name,
                                                    username=username,
                                                    email=email,
                                                    password=password,
                                                    commit=True)

        created_user = CustomUser.objects.filter(email=email).first()

        # Assert
        self.assertIsNotNone(created_user)

    def test_create_custom_user_should_add_new_user_when_commit_is_not_given(self):
        first_name = 'joey'
        last_name = 'dias'
        username = 'joey dias'
        email = 'test_user_1@gmail.com'
        password = 'dias123'

        # Act
        user = CustomUserService.create_custom_user(first_name=first_name,
                                                    last_name=last_name,
                                                    username=username,
                                                    email=email,
                                                    password=password)

        created_user = CustomUser.objects.filter(email=email).first()

        self.assertIsNotNone(created_user)

    def test_create_custom_user_should_not_add_user_when_commit_is_false(self):
        first_name = 'joey'
        last_name = 'dias'
        username = 'joey dias'
        email = 'test_user_2@gmail.com'
        password = 'dias123'

        CustomUserService.create_custom_user(first_name=first_name,
                                             last_name=last_name,
                                             username=username,
                                             email=email,
                                             password=password,
                                             commit=False)

        created_user = CustomUser.objects.filter(email=email).first()

        self.assertIsNone(created_user)

    def test_create_custom_user_should_raise_exception_when_the_email_is_already_used(self):
        # First User
        first_user_first_name = 'joey'
        first_user_last_name = 'dias'
        first_user_username = 'joeydias'
        first_user_email = 'test_user_1@gmail.com'
        first_user_password = 'dias123'

        # Creating the first user
        first_user = CustomUserService.create_custom_user(first_name=first_user_first_name,
                                                          last_name=first_user_last_name,
                                                          username=first_user_username,
                                                          email=first_user_email,
                                                          password=first_user_password)

        # Second user with the same email as the first user
        second_user_first_name = 'jane'
        second_user_last_name = 'doe'
        second_user_username = 'janedoe'
        second_user_email = 'test_user_1@gmail.com'
        second_user_password = 'doe123'

        # Using assertRaises to check if an IntegrityError is raised when trying to create the second user
        with transaction.atomic():
            # Use assertRaises to check if an IntegrityError is raised when trying to create the second user
            with self.assertRaises(IntegrityError) as context:
                CustomUserService.create_custom_user(first_name=second_user_first_name,
                                                     last_name=second_user_last_name,
                                                     username=second_user_username,
                                                     email=second_user_email,
                                                     password=second_user_password)

        # Verifying that the exception message contains the expected error message
        self.assertIn('duplicate key value violates unique constraint', str(context.exception))

    def test_get_user_by_id_should_return_user_when_id_is_passed(self):
        user = CustomUserService.get_user_by_id(_id=self.existing_user.id)

        self.assertEqual(self.existing_user, user)

    def test_get_user_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            user = CustomUserService.get_user_by_id(_id=-1)

        self.assertIn('CustomUser matching query does not exist', str(context.exception))

    def test_delete_user_should_delete_user_when_user_is_provided(self):
        CustomUserService.delete_user(self.existing_user)

        user_exists = CustomUser.objects.filter(email='random@gmail.com').exists()
        self.assertFalse(user_exists, "CustomUser object was not deleted")

    def test_delete_user_should_raise_exception_when_the_user_does_not_exist(self):
        random_user = CustomUserService.create_custom_user(first_name='random',
                                                           last_name='random',
                                                           username='random random',
                                                           email='random@abv.bg',
                                                           password='random123')

        CustomUserService.delete_user(random_user)

        with self.assertRaises(ValueError) as context:
            CustomUserService.delete_user(random_user)

        self.assertIn('CustomUser object can\'t be deleted because its id attribute is set to None', str(context.exception))

    def test_delete_user_by_id_should_delete_user_when_valid_id_is_provided(self):
        random_user = {
            'first_name': 'random',
            'last_name': 'random',
            'username': 'random random',
            'email': 'random_random@gmail.com',
            'password': 'random123'
        }

        current_user = CustomUserService.create_custom_user(**random_user)

        CustomUserService.delete_user_by_id(_id=current_user.id)

    def test_delete_user_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            CustomUserService.delete_user_by_id(_id=-100)

        self.assertIn('CustomUser matching query does not exist', str(context.exception))

    def test_update_user_by_id_should_update_user_when_commit_is_not_given(self):
        random_user = {
            'first_name': 'random',
            'last_name': 'random',
            'username': 'random random',
            'email': 'test_user_random_1@gmail.com',
            'password': 'random123'
        }

        random_user_new_credentials = {
            'first_name': 'random new',
            'last_name': 'random new',
            'username': 'random random new',
            'email': 'test_user_random_2@gmail.com',
            'password': 'random_new123'
        }

        current_user = CustomUserService.create_custom_user(**random_user)

        CustomUserService.edit_user_by_id(current_user.id, **random_user_new_credentials)

        changed_user = CustomUserService.get_user_by_id(current_user.id)

        self.assertEqual(random_user_new_credentials['first_name'], changed_user.first_name)
        self.assertEqual(random_user_new_credentials['last_name'], changed_user.last_name)
        self.assertEqual(random_user_new_credentials['username'], changed_user.username)
        self.assertEqual(random_user_new_credentials['email'], changed_user.email)
        self.assertTrue(changed_user.check_password(random_user_new_credentials['password']))


if __name__ == '__main__':
    unittest.main()
