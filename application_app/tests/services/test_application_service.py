from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from accounts_app.models import CustomUser
from application_app.models import Application
from application_app.models.job_offer_application_details import JobOfferApplicationDetails
from application_app.models.project_application_details import ProjectApplicationDetails
from services.generic.accounts_app.custom_user_service import CustomUserService
from services.generic.accounts_app.profile_service import ProfileService
from services.generic.application_app.application_service import ApplicationService
from services.generic.application_app.job_offer_application_details_service import JobOfferApplicationDetailsService
from services.generic.application_app.project_application_details_service import ProjectApplicationDetailsService
from services.generic.listing_app.listing_service import ListingService


class TestApplicationService(TestCase):
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

        listing_info = {
            'title': 'test_title',
            'location': 'test_location',
            'description': 'test_description',
        }
        self.random_listing = ListingService.create_listing(**listing_info)

        self.random_project_application = ProjectApplicationDetailsService.create_project_details(
            motivation_letter='random message'
        )

    def tearDown(self):
        CustomUser.objects.filter(email__startswith='test_user').delete()

    def test_create_application_should_add_new_application_when_commit_is_not_given(self):
        application = ApplicationService.create_application(profile=self.random_profile,
                                                            listing=self.random_listing,
                                                            content_type=ContentType.objects.get_for_model(
                                                                ProjectApplicationDetails),
                                                            object_id=self.random_project_application.id)

        last_added_application = Application.objects.latest('id')

        self.assertEqual(application, last_added_application)
        self.assertEqual(application.listing, last_added_application.listing)
        self.assertEqual(application.profile, last_added_application.profile)
        self.assertEqual(application.content_type, last_added_application.content_type)
        self.assertEqual(application.object_id, last_added_application.object_id)

    def test_create_application_should_add_new_application_when_commit_is_true(self):
        application = ApplicationService.create_application(profile=self.random_profile,
                                                            listing=self.random_listing,
                                                            content_type=ContentType.objects.get_for_model(
                                                                ProjectApplicationDetails),
                                                            object_id=self.random_project_application.id,
                                                            commit=True)

        last_added_application = Application.objects.latest('id')

        self.assertEqual(application, last_added_application)
        self.assertEqual(application.listing, last_added_application.listing)
        self.assertEqual(application.profile, last_added_application.profile)
        self.assertEqual(application.content_type, last_added_application.content_type)
        self.assertEqual(application.object_id, last_added_application.object_id)

    def test_create_application_should_not_add_application_when_commit_is_false(self):
        application = ApplicationService.create_application(profile=self.random_profile,
                                                            listing=self.random_listing,
                                                            content_type=ContentType.objects.get_for_model(
                                                                ProjectApplicationDetails),
                                                            object_id=self.random_project_application.id,
                                                            commit=False)

        last_added_application = Application.objects.last()
        self.assertIsNone(last_added_application)

    def test_create_application_should_add_application_when_content_type_is_job_offer_application_details(self):
        job_offer_application_details = JobOfferApplicationDetailsService.create_job_offer_details(cv='default/cv.png',
                                                                                                   motivation_letter='random message')

        application = ApplicationService.create_application(profile=self.random_profile,
                                                            listing=self.random_listing,
                                                            content_type=ContentType.objects.get_for_model(
                                                                JobOfferApplicationDetails),
                                                            object_id=job_offer_application_details.id,
                                                            commit=True)

        last_added_application = Application.objects.last()

        self.assertEqual(application, last_added_application)
        self.assertEqual(application.listing, last_added_application.listing)
        self.assertEqual(application.profile, last_added_application.profile)
        self.assertEqual(application.content_type, last_added_application.content_type)
        self.assertEqual(application.object_id, last_added_application.object_id)

    def test_get_all_application_should_return_all_applications(self):
        for i in range(0, 5):
            project_application_details = ProjectApplicationDetailsService.create_project_details(
                motivation_letter=f'random message {i}'
            )

            application = ApplicationService.create_application(profile=self.random_profile,
                                                                listing=self.random_listing,
                                                                content_type=ContentType.objects.get_for_model(
                                                                    ProjectApplicationDetails),
                                                                object_id=project_application_details.id)

        applications = ApplicationService.get_all_applications()
        self.assertEqual(applications.count(), 5)

    def test_get_application_by_id_should_return_application_when_id_is_passed(self):
        existing_application = ApplicationService.create_application(profile=self.random_profile,
                                                                     listing=self.random_listing,
                                                                     content_type=ContentType.objects.get_for_model(
                                                                        ProjectApplicationDetails),
                                                                     object_id=self.random_project_application.id)

        application = ApplicationService.get_application_by_id(_id=existing_application.id)
        self.assertEqual(existing_application, application)

    def test_get_application_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            ApplicationService.get_application_by_id(_id=-1)

        self.assertIn('Application matching query does not exist.', str(context.exception))

    def test_delete_application_should_delete_application_when_application_is_provided(self):
        existing_application = ApplicationService.create_application(profile=self.random_profile,
                                                                     listing=self.random_listing,
                                                                     content_type=ContentType.objects.get_for_model(
                                                                         ProjectApplicationDetails),
                                                                     object_id=self.random_project_application.id)

        ApplicationService.delete_application(existing_application)

    def test_delete_application_should_raise_exception_when_the_application_does_not_exist(self):
        application = ApplicationService.create_application(profile=self.random_profile,
                                                            listing=self.random_listing,
                                                            content_type=ContentType.objects.get_for_model(
                                                                 ProjectApplicationDetails),
                                                            object_id=self.random_project_application.id)

        ApplicationService.delete_application(application)
        with self.assertRaises(ValueError) as context:
            ApplicationService.delete_application(application)

        self.assertIn('Application object can\'t be deleted because its id attribute is set to None', str(context.exception))

    def test_delete_application_by_id_should_delete_application_when_valid_id_is_provided(self):
        application = ApplicationService.create_application(profile=self.random_profile,
                                                            listing=self.random_listing,
                                                            content_type=ContentType.objects.get_for_model(
                                                                ProjectApplicationDetails),
                                                            object_id=self.random_project_application.id)

        ApplicationService.delete_application_by_id(application.id)
        try:
            deleted_application = ApplicationService.get_application_by_id(_id=application.id)
        except ObjectDoesNotExist:
            deleted_application = None

        self.assertIsNone(deleted_application)

    def test_delete_application_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            CustomUserService.delete_user_by_id(_id=-100)

        self.assertIn('CustomUser matching query does not exist.', str(context.exception))

    def test_update_application_by_id_should_update_application_when_commit_is_not_given(self):
        application = ApplicationService.create_application(profile=self.random_profile,
                                                            listing=self.random_listing,
                                                            content_type=ContentType.objects.get_for_model(
                                                                ProjectApplicationDetails),
                                                            object_id=self.random_project_application.id)

        new_user_credentials = {
            'first_name': 'test',
            'last_name': 'test',
            'username': 'test test',
            'email': 'test_random_user_user@gmail.com',
            'password': 'password123',
        }
        new_user = CustomUserService.create_custom_user(**new_user_credentials)

        new_profile_credentials = {
            'user': new_user,
            'job_title': 'test_job',
            'description': 'test_description',
            'image_path': '/default/test_img.jpg'
        }
        new_profile = ProfileService.create_profile(**new_profile_credentials)

        listing_info = {
            'title': 'test_title',
            'location': 'test_location',
            'description': 'test_description',
        }
        new_listing = ListingService.create_listing(**listing_info)
        new_content_type = ContentType.objects.get_for_model(JobOfferApplicationDetails)

        ApplicationService.edit_application_by_id(_id=application.id,
                                                  profile=new_profile,
                                                  listing=new_listing,
                                                  content_type=new_content_type)

        changed_application = ApplicationService.get_application_by_id(_id=application.id)
        self.assertEqual(new_profile, changed_application.profile)
        self.assertEqual(new_listing, changed_application.listing)
        self.assertEqual(new_content_type, changed_application.content_type)
