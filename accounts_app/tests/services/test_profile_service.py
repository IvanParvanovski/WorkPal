from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from accounts_app.models import CustomUser
from accounts_app.models.profile import Profile
from services.generic.accounts_app.custom_user_service import CustomUserService
from services.generic.accounts_app.profile_service import ProfileService


class TestProfileService(TestCase):
    def setUp(self):
        random_user_credentials = {
            'first_name': 'test',
            'last_name': 'test',
            'username': 'test test',
            'email': 'test_random_user@gmail.com',
            'password': 'password123',
        }
        self.existing_user = CustomUserService.create_custom_user(**random_user_credentials)

        random_profile_credentials = {
            'user': self.existing_user,
            'job_title': 'test_job',
            'description': 'test_description',
            'image_path': '/default/test_img.jpg'
        }

        self.random_profile = ProfileService.create_profile(**random_profile_credentials)

    def tearDown(self):
        CustomUser.objects.filter(email__startswith='test_user').delete()

    def test_create_profile_should_add_new_profile_when_commit_is_not_given(self):
        test_user_credentials = {
            'first_name': 'test',
            'last_name': 'test',
            'username': 'test test',
            'email': 'test_user@gmail.com',
            'password': 'password123',
        }
        random_user = CustomUserService.create_custom_user(**test_user_credentials)

        test_profile_credentials = {
            'user': random_user,
            'job_title': 'test_job',
            'description': 'test_description',
            'image_path': '/default/test_img.jpg'
        }
        test_profile = ProfileService.create_profile(**test_profile_credentials)

        self.assertEqual(random_user, test_profile.user)
        self.assertEqual(test_profile_credentials['job_title'], test_profile.job_title)
        self.assertEqual(test_profile_credentials['description'], test_profile.description)
        self.assertEqual(test_profile_credentials['image_path'], test_profile.image)

    def test_create_profile_should_add_new_profile_when_commit_is_true(self):
        test_user_credentials = {
            'first_name': 'test',
            'last_name': 'test',
            'username': 'test test',
            'email': 'test_user@gmail.com',
            'password': 'password123',
        }
        random_user = CustomUserService.create_custom_user(**test_user_credentials)

        test_profile_credentials = {
            'user': random_user,
            'job_title': 'test_job',
            'description': 'test_description',
            'image_path': '/default/test_img.jpg'
        }
        test_profile = ProfileService.create_profile(**test_profile_credentials, commit=True)

        created_profile = Profile.objects.filter(user_id=random_user.id).first()
        self.assertIsNotNone(created_profile)
        self.assertEqual(created_profile, test_profile)

    def test_create_profile_should_not_add_profile_when_commit_is_false(self):
        test_user_credentials = {
            'first_name': 'test',
            'last_name': 'test',
            'username': 'test test',
            'email': 'test_user@gmail.com',
            'password': 'password123',
        }
        random_user = CustomUserService.create_custom_user(**test_user_credentials)

        test_profile_credentials = {
            'user': random_user,
            'job_title': 'test_job',
            'description': 'test_description',
            'image_path': '/default/test_image.jpg'
        }
        test_profile = ProfileService.create_profile(**test_profile_credentials, commit=False)
        created_profile = Profile.objects.filter(user_id=random_user.id).first()

        self.assertIsNone(created_profile)

    def test_get_all_profiles_should_return_all_profiles(self):
        test_user_credentials = {
            'first_name': 'test',
            'last_name': 'test',
            'username': 'test test',
            'email': 'test_user@gmail.com',
            'password': 'password123',
        }
        for i in range(0, 5):
            random_user = CustomUserService.create_custom_user(first_name=f'{test_user_credentials["first_name"]}_{i}',
                                                               last_name=f'{test_user_credentials["last_name"]}_{i}',
                                                               username=f'{test_user_credentials["username"]}_{i}',
                                                               email=f'{test_user_credentials["email"]}_{i}',
                                                               password=f'{test_user_credentials["password"]}_{i}')
            test_profile_credentials = {
                'user': random_user,
                'job_title': 'test_job',
                'description': 'test_description',
                'image_path': '/default/test_image.jpg'
            }
            ProfileService.create_profile(**test_profile_credentials)

        profiles = ProfileService.get_all_profiles()

        # They should be six with one default
        self.assertEqual(profiles.count(), 6)

    def test_get_profile_by_id_should_return_profile_when_id_is_passed(self):
        profile = ProfileService.get_profile_by_id(_id=self.random_profile.id)
        self.assertEqual(self.random_profile, profile)

    def test_get_profile_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            ProfileService.get_profile_by_id(_id=-1)

        self.assertEqual('Profile matching query does not exist.', str(context.exception))

    def test_delete_profile_should_delete_profile_when_profile_is_provided(self):
        ProfileService.delete_profile(self.random_profile)
        profile_exists = Profile.objects.filter(user=self.existing_user)
        self.assertFalse(profile_exists, 'Profile was not deleted')

    def test_delete_profile_should_raise_exception_when_the_profile_does_not_exist(self):
        ProfileService.delete_profile(self.random_profile)

        with self.assertRaises(ValueError) as context:
            ProfileService.delete_profile(self.random_profile)

        self.assertIn("Profile object can't be deleted because its id attribute is set to None.", str(context.exception))

    def test_delete_profile_by_id_should_delete_profile_when_valid_id_is_provided(self):
        profiles_count = ProfileService.get_all_profiles().count()
        ProfileService.delete_profile_by_id(self.random_profile.id)
        profiles_count_after_delete = ProfileService.get_all_profiles().count()

        self.assertEqual(profiles_count - 1, profiles_count_after_delete)

    def test_delete_profile_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            ProfileService.delete_profile_by_id(-1)

        self.assertIn('Profile matching query does not exist.', str(context.exception))

    def test_update_profile_by_id_should_update_profile_when_commit_is_not_given(self):
        new_profile_credentials = {
            'job_title': 'test new',
            'description': 'test new',
            'image_path': '/default/test_img_new.jpg'
        }

        ProfileService.edit_profile_by_id(self.random_profile.id,
                                          **new_profile_credentials)

        changed_profile = ProfileService.get_profile_by_id(self.random_profile.id)

        self.assertEqual(new_profile_credentials['job_title'], changed_profile.job_title)
        self.assertEqual(new_profile_credentials['description'], changed_profile.description)
