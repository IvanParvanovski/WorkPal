from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from services.generic.application_app.project_application_details_service import ProjectApplicationDetailsService


class TestProjectApplicationDetailsService(TestCase):
    def test_create_project_application_details_should_add_new_project_application_details_when_commit_is_not_given(
            self):
        motivation_letter = 'random motivation letter'
        project_application_details = ProjectApplicationDetailsService.create_project_details(
            motivation_letter=motivation_letter)

        try:
            created_details = ProjectApplicationDetailsService.get_project_details_by_id(project_application_details.id)
        except ObjectDoesNotExist:
            created_details = None

        self.assertIsNotNone(created_details)
        self.assertEqual(created_details, project_application_details)
        self.assertEqual(motivation_letter, created_details.motivation_letter)
        self.assertEqual(motivation_letter, project_application_details.motivation_letter)

    def test_create_project_application_details_should_add_new_project_application_details_when_commit_is_true(self):
        motivation_letter = 'random motivation letter'
        project_application_details = ProjectApplicationDetailsService.create_project_details(
            motivation_letter=motivation_letter,
            commit=True
        )

        try:
            created_details = ProjectApplicationDetailsService.get_project_details_by_id(project_application_details.id)
        except ObjectDoesNotExist:
            created_details = None

        self.assertIsNotNone(created_details)
        self.assertEqual(created_details, project_application_details)
        self.assertEqual(motivation_letter, created_details.motivation_letter)
        self.assertEqual(motivation_letter, project_application_details.motivation_letter)

    def test_create_project_application_details_should_not_add_project_application_details_when_commit_is_false(self):
        motivation_letter = 'random motivation letter'
        project_application_details = ProjectApplicationDetailsService.create_project_details(
            motivation_letter=motivation_letter,
            commit=False
        )

        try:
            created_details = ProjectApplicationDetailsService.get_project_details_by_id(
                project_application_details.id)
        except ObjectDoesNotExist:
            created_details = None

        self.assertIsNone(created_details)

    def test_get_all_project_application_details_should_return_all_projects_application_details(self):
        motivation_letter = 'random motivation letter'

        for i in range(0, 5):
            project_application_details = (ProjectApplicationDetailsService
                                           .create_project_details(motivation_letter=f'{motivation_letter}_{i}'))

        projects_application_details_count = ProjectApplicationDetailsService.get_all_project_details().count()

        self.assertEqual(5, projects_application_details_count)

    def test_get_project_application_details_by_id_should_return_details_when_id_is_passed(self):
        motivation_letter = 'random motivation letter'

        project_application_details = ProjectApplicationDetailsService.create_project_details(motivation_letter=motivation_letter)
        returned_object = ProjectApplicationDetailsService.get_project_details_by_id(_id=project_application_details.id)

        self.assertEqual(project_application_details, returned_object)

    def test_get_project_application_details_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            ProjectApplicationDetailsService.get_project_details_by_id(_id=-1)

        self.assertEqual('ProjectApplicationDetails matching query does not exist.', str(context.exception))

    def test_delete_project_application_details_should_delete_details_when_project_application_details_is_provided(self):
        motivation_letter = 'random motivation letter'

        project_application_details = ProjectApplicationDetailsService.create_project_details(motivation_letter)

        try:
            created_entity = ProjectApplicationDetailsService.get_project_details_by_id(project_application_details.id)
        except ObjectDoesNotExist:
            created_entity = None

        self.assertIsNotNone(created_entity)

        ProjectApplicationDetailsService.delete_project_details(project_application_details)

        try:
            created_entity = ProjectApplicationDetailsService.get_project_details_by_id(project_application_details.id)
        except ObjectDoesNotExist:
            created_entity = None

        self.assertIsNone(created_entity)

    def test_delete_project_application_details_should_raise_exception_when_the_details_does_not_exist(self):
        motivation_letter = 'random motivation letter'

        project_application_details = ProjectApplicationDetailsService.create_project_details(motivation_letter)
        ProjectApplicationDetailsService.delete_project_details(project_application_details)

        with self.assertRaises(ValueError) as context:
            ProjectApplicationDetailsService.delete_project_details(project_application_details)

        self.assertIn('ProjectApplicationDetails object can\'t be deleted because its id attribute is set to None.', str(context.exception))

    def test_delete_project_application_details_by_id_should_delete_details_when_valid_id_is_provided(self):
        motivation_letter = 'random motivation letter'
        project_application_details = ProjectApplicationDetailsService.create_project_details(motivation_letter)

        try:
            created_entity = ProjectApplicationDetailsService.get_project_details_by_id(project_application_details.id)
        except ObjectDoesNotExist:
            created_entity = None

        self.assertIsNotNone(created_entity)

    def test_delete_project_application_details_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            ProjectApplicationDetailsService.get_project_details_by_id(_id=-1)

        self.assertEqual('ProjectApplicationDetails matching query does not exist.', str(context.exception))

    def test_update_project_application_details_by_id_should_update_details_when_commit_is_not_given(self):
        motivation_letter = 'random motivation letter'
        new_motivation_letter = 'new motivation letter'

        project_application_details = ProjectApplicationDetailsService.create_project_details(motivation_letter)

        ProjectApplicationDetailsService.edit_project_details_by_id(_id=project_application_details.id,
                                                                    motivation_letter=new_motivation_letter)

        changed_project_application_details = (ProjectApplicationDetailsService
                                               .get_project_details_by_id(project_application_details.id))

        self.assertEqual(new_motivation_letter, changed_project_application_details.motivation_letter)
