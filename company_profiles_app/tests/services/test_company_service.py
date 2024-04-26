from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from company_profiles_app.models import Employment
from services.generic.accounts_app.custom_user_service import CustomUserService
from services.generic.accounts_app.profile_service import ProfileService
from services.generic.company_profiles_app.company_service import CompanyService
from services.generic.company_profiles_app.employment_service import EmploymentService


class CompanyServiceTestCase(TestCase):
    def setUp(self):
        self.random_company_data = {
            'address': 'test address',
            'secondary_address': 'test secondary address',
            'company_logo': 'default/logo.png',
            'name': 'random name',
            'website': 'https://www.google.com',
        }

    def test_create_company_should_create_company_when_commit_is_not_given(self):
        company = CompanyService.create_company(**self.random_company_data)

        try:
            result = CompanyService.get_company_by_id(_id=company.id)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNotNone(result)
        self.assertIsNotNone(company)
        self.assertEqual(self.random_company_data['address'], result.address)
        self.assertEqual(self.random_company_data['secondary_address'], result.secondary_address)
        self.assertEqual(self.random_company_data['name'], result.name)
        self.assertEqual(self.random_company_data['website'], result.website)

    def test_create_company_should_create_company_when_commit_is_true(self):
        company = CompanyService.create_company(**self.random_company_data, commit=True)

        try:
            result = CompanyService.get_company_by_id(_id=company.id)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNotNone(result)
        self.assertIsNotNone(company)
        self.assertEqual(self.random_company_data['address'], result.address)
        self.assertEqual(self.random_company_data['secondary_address'], result.secondary_address)
        self.assertEqual(self.random_company_data['name'], result.name)
        self.assertEqual(self.random_company_data['website'], result.website)

    def test_create_company_should_raise_exception_when_commit_is_false(self):
        company = CompanyService.create_company(**self.random_company_data, commit=False)

        try:
            result = CompanyService.get_company_by_id(_id=company.id)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_get_company_by_id_should_return_correct_company(self):
        company = CompanyService.create_company(**self.random_company_data)

        try:
            returned_object = CompanyService.get_company_by_id(_id=company.id)
        except ObjectDoesNotExist:
            returned_object = None

        self.assertIsNotNone(returned_object)

    def test_get_company_by_id_should_raise_exception_when_id_is_invalid(self):
        try:
            returned_object = CompanyService.get_company_by_id(_id=-1)
        except ObjectDoesNotExist:
            returned_object = None

        self.assertIsNone(returned_object)

    def test_get_user_associated_companies_should_return_correct_companies(self):
        user = CustomUserService.create_custom_user(
            first_name='random name',
            last_name='random name',
            username='random random',
            email='random@gmail.com',
            password='random'
        )
        profile = ProfileService.create_profile(
            user=user,
            job_title='random job title',
            description='random description',
            image_path='/random/img.png'
        )

        company_one = CompanyService.create_company(
            address='test address 1',
            secondary_address='test secondary address 1',
            company_logo='default/logo1.png',
            name='random name 1',
            website='https://www.google.com')
        company_two = CompanyService.create_company(
            address='test address 2',
            secondary_address='test secondary address 2',
            company_logo='default/logo2.png',
            name='random name 2',
            website='https://www.google.com')

        first_employment = EmploymentService.create_employment(
            profile=profile,
            company=company_one,
            job_title=Employment.CompanyRoles.EMPLOYEE
        )
        EmploymentService.set_employment_is_checked_to_true(employment=first_employment)
        EmploymentService.set_employment_is_associate_to_true(employment=first_employment)

        second_employment = EmploymentService.create_employment(
            profile=profile,
            company=company_two,
            job_title=Employment.CompanyRoles.HIRING_MANAGER
        )
        EmploymentService.set_employment_is_checked_to_true(employment=second_employment)
        EmploymentService.set_employment_is_associate_to_true(employment=second_employment)

        user_companies = CompanyService.get_user_companies(profile_id=profile.id)

        self.assertIn(company_one, user_companies)
        self.assertIn(company_two, user_companies)

    def test_delete_company_should_delete_company(self):
        company = CompanyService.create_company(**self.random_company_data)

        CompanyService.delete_company(company)

        try:
            result = CompanyService.get_company_by_id(_id=company.id)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_delete_company_by_id_should_delete_company(self):
        company = CompanyService.create_company(**self.random_company_data)

        CompanyService.delete_company_by_id(_id=company.id)

        try:
            result = CompanyService.get_company_by_id(company.id)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_delete_company_should_raise_exception_when_id_is_invalid(self):
        try:
            result = CompanyService.delete_company_by_id(_id=-1)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_edit_company_should_edit_company(self):
        new_company_data = {
            'address': 'new test address',
            'secondary_address': 'new secondary address',
            'name': 'new name',
            'company_logo': '/default/logo.png',
            'website': 'https://www.facebook.com'
        }

        company = CompanyService.create_company(**self.random_company_data)

        changed_company = CompanyService.edit_company(_id=company.id, **new_company_data)

        self.assertEqual(new_company_data['address'], changed_company.address)
        self.assertEqual(new_company_data['secondary_address'], changed_company.secondary_address)
        self.assertEqual(new_company_data['name'], changed_company.name)
        self.assertEqual(new_company_data['company_logo'], changed_company.company_logo)
        self.assertEqual(new_company_data['website'], changed_company.website)
