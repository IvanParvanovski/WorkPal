from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from company_profiles_app.models import Employment
from services.generic.accounts_app.custom_user_service import CustomUserService
from services.generic.accounts_app.profile_service import ProfileService
from services.generic.company_profiles_app.company_service import CompanyService
from services.generic.company_profiles_app.employment_service import EmploymentService


class EmploymentServiceTestCase(TestCase):
    def setUp(self):
        self.user = CustomUserService.create_custom_user(
            first_name='random name',
            last_name='random name',
            username='random random',
            email='random@gmail.com',
            password='random'
        )
        self.profile = ProfileService.create_profile(
            user=self.user,
            job_title='random title',
            description='random description',
            image_path='path/to/image',
        )
        self.company = CompanyService.create_company(
            address='random address',
            secondary_address='random secondary address',
            name='random name',
            company_logo='path/to/logo.png',
            website='https://www.google.com',
        )

    def tearDown(self):
        pass

    def test_create_employment_should_create_new_employment_when_commit_is_not_given(self):
        employment = EmploymentService.create_employment(profile=self.profile,
                                                         company=self.company,
                                                         job_title='random title')

        created_employment = EmploymentService.get_employment_by_id(employment.id)

        self.assertEqual(employment.profile, created_employment.profile)
        self.assertEqual(employment.company, created_employment.company)
        self.assertEqual(employment.job_title, created_employment.job_title)

    def test_create_employment_should_create_new_employment_when_commit_is_true(self):
        employment = EmploymentService.create_employment(profile=self.profile,
                                                         company=self.company,
                                                         job_title=Employment.CompanyRoles.HIRING_MANAGER,
                                                         commit=True)

        created_employment = EmploymentService.get_employment_by_id(employment.id)

        self.assertEqual(employment.profile, created_employment.profile)
        self.assertEqual(employment.company, created_employment.company)
        self.assertEqual(employment.job_title, created_employment.job_title)

    def test_create_employment_should_not_create_new_employment_when_commit_is_false(self):
        employment = EmploymentService.create_employment(profile=self.profile,
                                                         company=self.company,
                                                         job_title=Employment.CompanyRoles.HIRING_MANAGER,
                                                         commit=False)

        try:
            created_employment = EmploymentService.get_employment_by_id(employment.id)
        except ObjectDoesNotExist:
            created_employment = None

        self.assertIsNone(created_employment)

    def test_get_all_employments_should_return_all_employments(self):
        for _ in range(0, 5):
            EmploymentService.create_employment(profile=self.profile,
                                                company=self.company,
                                                job_title=Employment.CompanyRoles.HIRING_MANAGER)

        employments = EmploymentService.get_all_employments()
        self.assertEqual(5, employments.count())

    def test_get_employment_by_id_should_return_employment(self):
        employment = EmploymentService.create_employment(profile=self.profile,
                                                         company=self.company,
                                                         job_title=Employment.CompanyRoles.HIRING_MANAGER)

        try:
            returned_object = EmploymentService.get_employment_by_id(_id=employment.id)
        except ObjectDoesNotExist:
            returned_object = None

        self.assertIsNotNone(returned_object)

    def test_get_employment_by_id_should_raise_exception_when_id_is_invalid(self):
        employment = EmploymentService.create_employment(profile=self.profile,
                                                         company=self.company,
                                                         job_title=Employment.CompanyRoles.HIRING_MANAGER)

        try:
            returned_object = EmploymentService.get_employment_by_id(employment.id)
        except ObjectDoesNotExist:
            returned_object = None

        self.assertIsNotNone(returned_object)
        self.assertEqual(employment, returned_object)

    def test_get_associates_for_company_should_return_company_associates(self):
        user_one = CustomUserService.create_custom_user(
            first_name='random name 1',
            last_name='random name 1',
            username='random random 1',
            email='random@gmail.com1',
            password='random1'
        )
        profile_one = ProfileService.create_profile(
            user=user_one,
            job_title='random title 1',
            description='random description',
            image_path='path/to/image',
        )
        employment_one = EmploymentService.create_employment(profile=profile_one,
                                                             company=self.company,
                                                             job_title=Employment.CompanyRoles.HIRING_MANAGER)
        EmploymentService.set_employment_is_associate_to_true(employment_one)
        EmploymentService.set_employment_is_checked_to_true(employment_one)

        user_two = CustomUserService.create_custom_user(
            first_name='random name2',
            last_name='random name2',
            username='random random2',
            email='random@gmail.com2',
            password='random2'
        )
        profile_two = ProfileService.create_profile(
            user=user_two,
            job_title='random title',
            description='random description',
            image_path='path/to/image',
        )
        employment_two = EmploymentService.create_employment(profile=profile_two,
                                                             company=self.company,
                                                             job_title=Employment.CompanyRoles.EMPLOYEE)
        EmploymentService.set_employment_is_checked_to_true(employment_two)
        EmploymentService.set_employment_is_associate_to_true(employment_two)

        company_associates = EmploymentService.get_associates_for_company(self.company)

        self.assertIn(employment_one, company_associates)
        self.assertIn(employment_two, company_associates)

    def test_get_association_requests_for_company_should_return_company_associates(self):
        employment_one = EmploymentService.create_employment(profile=self.profile,
                                                             company=self.company,
                                                             job_title=Employment.CompanyRoles.HIRING_MANAGER)
        employment_two = EmploymentService.create_employment(profile=self.profile,
                                                             company=self.company,
                                                             job_title=Employment.CompanyRoles.HIRING_MANAGER)

        association_requests = EmploymentService.get_association_requests_for_company(self.company)

        self.assertIn(employment_one, association_requests)
        self.assertIn(employment_two, association_requests)

    def test_delete_employment_should_delete_employment(self):
        employment = EmploymentService.create_employment(profile=self.profile,
                                                         company=self.company,
                                                         job_title=Employment.CompanyRoles.HIRING_MANAGER)

        EmploymentService.delete_employment(employment)

        try:
            response = EmploymentService.get_employment_by_id(employment.id)
        except ObjectDoesNotExist:
            response = None

        self.assertIsNone(response)

    def test_delete_employment_by_id_should_delete_employment(self):
        employment = EmploymentService.create_employment(profile=self.profile,
                                                         company=self.company,
                                                         job_title=Employment.CompanyRoles.EMPLOYEE)

        EmploymentService.delete_employment_by_id(employment.id)

        try:
            response = EmploymentService.get_employment_by_id(employment.id)
        except ObjectDoesNotExist:
            response = None

        self.assertIsNone(response)

    def test_delete_employment_by_id_should_raise_exception_when_id_is_invalid(self):
        try:
            response = EmploymentService.delete_employment_by_id(-1)
        except ObjectDoesNotExist:
            response = None

        self.assertIsNone(response)

    def test_set_employment_is_associate_to_true_should_set_it_to_true(self):
        employment = EmploymentService.create_employment(profile=self.profile,
                                                         company=self.company,
                                                         job_title=Employment.CompanyRoles.EMPLOYEE)

        EmploymentService.set_employment_is_associate_to_true(employment)

        self.assertEqual(True, employment.is_associate)

    def test_set_employment_is_checked_to_true_should_set_it_to_true(self):
        employment = EmploymentService.create_employment(profile=self.profile,
                                                         company=self.company,
                                                         job_title=Employment.CompanyRoles.EMPLOYEE)

        EmploymentService.set_employment_is_checked_to_true(employment)

        self.assertEqual(True, employment.is_checked)

    def test_edit_employment_should_edit_employment(self):
        employment = EmploymentService.create_employment(profile=self.profile,
                                                         company=self.company,
                                                         job_title=Employment.CompanyRoles.EMPLOYEE)
        user_new = CustomUserService.create_custom_user(
            first_name='random name new',
            last_name='random name new',
            username='random random new',
            email='random@gmail.com_new',
            password='random_new'
        )
        profile_new = ProfileService.create_profile(
            user=user_new,
            job_title='random title new',
            description='random description new',
            image_path='path/to/image_new',
        )
        company_new = CompanyService.create_company(
            address='random address new',
            secondary_address='random secondary address new',
            name='random name new',
            company_logo='path/to/logo_new.png',
            website='https://www.google.com_new',
        )
        job_title_new = Employment.CompanyRoles.EMPLOYEE

        EmploymentService.edit_employment_by_id(_id=employment.id,
                                                profile=profile_new,
                                                company=company_new,
                                                job_title=job_title_new)

        changed_object = EmploymentService.get_employment_by_id(_id=employment.id)

        self.assertEqual(profile_new, changed_object.profile)
        self.assertEqual(company_new, changed_object.company)
        self.assertEqual(job_title_new, changed_object.job_title)
