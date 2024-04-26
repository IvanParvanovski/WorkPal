from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from services.generic.company_profiles_app.company_identifiers_service import CompanyIdentifiersService
from services.generic.company_profiles_app.company_service import CompanyService


class CompanyIdentifiersServiceTestCase(TestCase):
    def setUp(self):
        self.company = CompanyService.create_company(
            address='test address',
            secondary_address='test secondary address',
            name='test company',
            company_logo='default/logo/logo.png',
            website='https://test.com'
        )

    def test_create_company_identifier_should_create_company_identifier_when_commit_is_not_given(self):
        company_identifier = CompanyIdentifiersService.create_company_identifier(
            _type='email',
            value='random@random.com',
            company=self.company
        )

        self.assertEqual('email', company_identifier.type),
        self.assertEqual('random@random.com', company_identifier.value)
        self.assertEqual(self.company, company_identifier.company)

    def test_create_company_identifier_should_create_company_identifier_when_commit_is_true(self):
        company_identifier = CompanyIdentifiersService.create_company_identifier(
            _type='email',
            value='random@random.com',
            company=self.company,
            commit=True
        )

        self.assertEqual('email', company_identifier.type)
        self.assertEqual('random@random.com', company_identifier.value)
        self.assertEqual(self.company, company_identifier.company)

    def test_create_company_identifier_should_not_create_company_identifier_when_commit_is_false(self):
        company_identifier = CompanyIdentifiersService.create_company_identifier(
            _type='email',
            value='random@random.com',
            company=self.company,
            commit=False
        )

        try:
            created_object = CompanyIdentifiersService.get_identifier_by_id(_id=company_identifier.id)
        except ObjectDoesNotExist:
            created_object = None

        self.assertIsNone(created_object)

    def test_create_company_identifier_email_should_create_company_identifier_with_email(self):
        company_identifier = CompanyIdentifiersService.create_company_identifier_email(value='random@random.com',
                                                                                       company=self.company)

        self.assertEqual('email', company_identifier.type)
        self.assertEqual('random@random.com', company_identifier.value)
        self.assertEqual(self.company, company_identifier.company)

    def test_create_company_identifier_phone_number_should_create_company_identifier_with_phone_number(self):
        company_identifier = CompanyIdentifiersService.create_company_identifier_phone_number(value='081582351',
                                                                                              company=self.company)

        self.assertEqual('phone_number', company_identifier.type)
        self.assertEqual('081582351', company_identifier.value)
        self.assertEqual(self.company, company_identifier.company)

    def test_get_company_identifier_phone_number_should_return_correct_phone_number(self):
        company_identifier = CompanyIdentifiersService.create_company_identifier_phone_number(value='081582351',
                                                                                              company=self.company)

        identifier = CompanyIdentifiersService.get_company_identifier_phone_number(company_id=self.company.id)

        self.assertEqual('081582351', identifier.value)

    def test_get_company_identifier_email_should_return_correct_email(self):
        company_identifier = CompanyIdentifiersService.create_company_identifier_email(value='random@random.com',
                                                                                       company=self.company)

        identifier = CompanyIdentifiersService.get_company_identifier_email(company_id=self.company.id)
        self.assertEqual('random@random.com', identifier.value)

    def test_get_identifier_by_id_should_return_correct_company_identifier(self):
        company_identifier = CompanyIdentifiersService.create_company_identifier_email(value='random@random.com',
                                                                                       company=self.company)

        returned_object = CompanyIdentifiersService.get_identifier_by_id(company_identifier.id)

        self.assertEqual(company_identifier, returned_object)

    def test_get_identifier_by_id_should_raise_exception_if_id_is_invalid(self):
        try:
            result = CompanyIdentifiersService.get_identifier_by_id(-1)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_delete_identifier_should_delete_company_identifier_when_it_exists(self):
        identifier = CompanyIdentifiersService.create_company_identifier_email(value='random@random.com',
                                                                               company=self.company)

        CompanyIdentifiersService.delete_identifier(identifier)

        try:
            result = CompanyIdentifiersService.get_identifier_by_id(identifier.id)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_delete_identifier_by_id_should_delete_company_identifier_when_it_exists(self):
        identifier = CompanyIdentifiersService.create_company_identifier_email(value='random@random.com',
                                                                               company=self.company)

        CompanyIdentifiersService.delete_identifier_by_id(identifier.id)

        try:
            result = CompanyIdentifiersService.get_identifier_by_id(identifier.id)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_delete_identifier_by_id_should_raise_exception_if_id_is_invalid(self):
        try:
            result = CompanyIdentifiersService.delete_identifier_by_id(-1)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_edit_identifier_by_id_should_edit_company_identifier_when_it_exists(self):
        new_company = CompanyService.create_company(
            address='new test address',
            secondary_address='new test secondary address',
            name='new test company',
            company_logo='default/logo_new/logo.png',
            website='https://test.com_new'
        )

        identifier = CompanyIdentifiersService.create_company_identifier_email(value='random@random.com_new',
                                                                               company=self.company)

        CompanyIdentifiersService.edit_identifier_by_id(_id=identifier.id,
                                                        _type='phone_number',
                                                        value='081582351',
                                                        company=new_company)
        changed_identifier = CompanyIdentifiersService.get_identifier_by_id(identifier.id)

        self.assertEqual('phone_number', changed_identifier.type)
        self.assertEqual('081582351', changed_identifier.value)
        self.assertEqual(new_company, changed_identifier.company)
