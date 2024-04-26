from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from listing_app.models.listing import Listing
from listing_app.models.project import Project
from services.generic.accounts_app.custom_user_service import CustomUserService
from services.generic.accounts_app.profile_service import ProfileService
from services.generic.listing_app.listing_service import ListingService
from services.generic.listing_app.project_service import ProjectService


class ProjectServiceTestCase(TestCase):
    def setUp(self):
        self.listing = ListingService.create_listing(
            title='Test Project',
            description='Test description',
            location='Test location',
        )
        self.user = CustomUserService.create_custom_user(
            first_name='Test',
            last_name='Test',
            username='test test',
            email='test@test.com',
            password='test',
        )
        self.profile = ProfileService.create_profile(
            user=self.user,
            job_title='Test Job title',
            description='Test description',
            image_path='default/test.png',
        )
        self.random_project_data = {
            'profile': self.profile,
            'listing': self.listing,
            'wage': 1,
            'preferred_payment': 'random',
            'status': Project.Status.OPEN,
            'estimated_duration': 'random time'
        }

    def test_create_project_should_add_new_project_when_commit_is_not_given(self):
        project = ProjectService.create_project(**self.random_project_data)

        try:
            created_project = ProjectService.get_project_by_id(project.id)
        except ObjectDoesNotExist:
            created_project = None

        self.assertIsNotNone(created_project)

        self.assertEqual(self.random_project_data['profile'], project.profile)
        self.assertEqual(self.random_project_data['listing'], project.listing)
        self.assertEqual(self.random_project_data['wage'], project.wage)
        self.assertEqual(self.random_project_data['preferred_payment'], project.preferred_payment)
        self.assertEqual(self.random_project_data['status'], project.status)
        self.assertEqual(self.random_project_data['estimated_duration'], project.estimated_duration)

    def test_create_project_should_add_new_project_when_commit_is_true(self):
        project = ProjectService.create_project(**self.random_project_data, commit=True)

        try:
            created_project = ProjectService.get_project_by_id(project.id)
        except ObjectDoesNotExist:
            created_project = None

        self.assertIsNotNone(created_project)

    def test_create_project_should_add_new_project_when_commit_is_false(self):
        project = ProjectService.create_project(**self.random_project_data, commit=False)

        try:
            created_project = ProjectService.get_project_by_id(project.id)
        except ObjectDoesNotExist:
            created_project = None

        self.assertIsNone(created_project)

    def test_get_all_projects_should_return_all_projects(self):
        new_listing_data = {
            'title': 'new test project',
            'description': 'new test description',
            'location': 'new test location',
        }

        listing_one = ListingService.create_listing(**new_listing_data)
        project_one = ProjectService.create_project(profile=self.random_project_data['profile'],
                                                    listing=listing_one,
                                                    wage=self.random_project_data['wage'],
                                                    preferred_payment=self.random_project_data['preferred_payment'],
                                                    status=self.random_project_data['status'],
                                                    estimated_duration=self.random_project_data['estimated_duration'])

        listing_two = ListingService.create_listing(**new_listing_data)
        project_two = ProjectService.create_project(profile=self.random_project_data['profile'],
                                                    listing=listing_two,
                                                    wage=self.random_project_data['wage'],
                                                    preferred_payment=self.random_project_data['preferred_payment'],
                                                    status=self.random_project_data['status'],
                                                    estimated_duration=self.random_project_data['estimated_duration'])

        listing_three = ListingService.create_listing(**new_listing_data)
        project_three = ProjectService.create_project(profile=self.random_project_data['profile'],
                                                      listing=listing_three,
                                                      wage=self.random_project_data['wage'],
                                                      preferred_payment=self.random_project_data['preferred_payment'],
                                                      status=self.random_project_data['status'],
                                                      estimated_duration=self.random_project_data['estimated_duration'])

        projects = ProjectService.get_all_projects()

        self.assertIn(project_one, projects)
        self.assertIn(project_two, projects),
        self.assertIn(project_three, projects)

    def test_get_project_by_id_should_return_project(self):
        project = ProjectService.create_project(**self.random_project_data)

        returned_project = ProjectService.get_project_by_id(_id=project.id)

        self.assertEqual(project, returned_project)

    def test_get_project_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            ProjectService.get_project_by_id(_id=-1)

        self.assertIn('Project matching query does not exist.', str(context.exception))

    def test_get_projects_by_profile_id_should_return_correct_projects(self):
        new_listing_data = {
            'title': 'new test project',
            'description': 'new test description',
            'location': 'new test location',
        }
        listing_one = ListingService.create_listing(**new_listing_data)
        listing_two = ListingService.create_listing(**new_listing_data)

        project_one = ProjectService.create_project(profile=self.random_project_data['profile'],
                                                    listing=listing_one,
                                                    wage=self.random_project_data['wage'],
                                                    preferred_payment=self.random_project_data['preferred_payment'],
                                                    status=self.random_project_data['status'],
                                                    estimated_duration=self.random_project_data['estimated_duration'])

        project_two = ProjectService.create_project(profile=self.random_project_data['profile'],
                                                    listing=listing_two,
                                                    wage=self.random_project_data['wage'],
                                                    preferred_payment=self.random_project_data['preferred_payment'],
                                                    status=self.random_project_data['status'],
                                                    estimated_duration=self.random_project_data['estimated_duration'])

        user_projects = ProjectService.get_projects_by_profile_id(_id=self.profile.id)

        self.assertIn(project_one, user_projects)
        self.assertIn(project_two, user_projects)

    def test_get_projects_by_profile_id_should_return_empty_list_when_id_is_invalid(self):
        try:
            result = ProjectService.get_projects_by_profile_id(_id=-1)
        except ObjectDoesNotExist:
            result = None

        self.assertEqual(0, result.count())

    def test_delete_project_should_delete_project_when_it_exists(self):
        project = ProjectService.create_project(**self.random_project_data)

        ProjectService.delete_project(project)

        try:
            result = ProjectService.get_project_by_id(_id=project.id)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_delete_project_by_id_should_delete_project_when_it_exists(self):
        project = ProjectService.create_project(**self.random_project_data)

        ProjectService.delete_project_by_id(_id=project.id)

        try:
            result = ProjectService.get_project_by_id(_id=project.id)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_delete_project_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            ProjectService.delete_project_by_id(_id=-1)

        self.assertIn('Project matching query does not exist.', str(context.exception))

    def test_edit_project_by_id_should_edit_project(self):
        project = ProjectService.create_project(**self.random_project_data)
        new_random_project_data = {
            'wage': 999,
            'preferred_payment': 'random random',
            'status': Project.Status.COMPLETED,
            'estimated_duration': 'new random time'
        }

        returned_object = ProjectService.edit_project_by_id(_id=project.id, **new_random_project_data)
        changed_project = ProjectService.get_project_by_id(_id=project.id)

        self.assertEqual(changed_project, returned_object)
        self.assertEqual(new_random_project_data['wage'], changed_project.wage)
        self.assertEqual(new_random_project_data['preferred_payment'], changed_project.preferred_payment)
        self.assertEqual(new_random_project_data['status'], changed_project.status)
        self.assertEqual(new_random_project_data['estimated_duration'], changed_project.estimated_duration)
