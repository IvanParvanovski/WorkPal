from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from services.generic.listing_app.industry_service import IndustryService


class IndustryServiceTestCase(TestCase):
    def test_create_industry_should_add_new_industry_when_commit_is_not_given(self):
        industry = IndustryService.create_industry(name='test industry')

        try:
            created_industry = IndustryService.get_industry_by_id(_id=industry.id)
        except ObjectDoesNotExist:
            created_industry = None

        self.assertIsNotNone(created_industry)
        self.assertEqual(industry.name, created_industry.name)

    def test_create_industry_should_add_new_industry_when_commit_is_true(self):
        industry = IndustryService.create_industry(name='test industry', commit=True)

        try:
            created_industry = IndustryService.get_industry_by_id(_id=industry.id)
        except ObjectDoesNotExist:
            created_industry = None

        self.assertIsNotNone(created_industry)
        self.assertEqual(industry.name, created_industry.name)

    def test_create_industry_should_add_new_industry_when_commit_is_false(self):
        industry = IndustryService.create_industry(name='test industry', commit=False)

        try:
            created_industry = IndustryService.get_industry_by_id(_id=industry.id)
        except ObjectDoesNotExist:
            created_industry = None

        self.assertIsNone(created_industry)

    def test_get_all_industries_should_return_all_industries(self):
        industries = [IndustryService.create_industry(name=f'test name_{i}') for i in range(0, 5)]

        returned_industries = IndustryService.get_all_industries()

        self.assertEqual(5, returned_industries.count())

        for industry in industries:
            self.assertIn(industry, industries)

    def test_get_industry_by_id_should_return_correct_industry(self):
        industry = IndustryService.create_industry(name='test industry')

        returned_object = IndustryService.get_industry_by_id(industry.id)

        self.assertEqual(industry, returned_object)

    def test_get_industry_by_id_should_raise_exception_when_id_is_invalid(self):
        try:
            result = IndustryService.get_industry_by_id(-1)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_get_industry_by_name_should_return_correct_industry(self):
        industry = IndustryService.create_industry(name='test industry')

        returned_industry = IndustryService.get_industry_by_id(_id=industry.id)

        self.assertEqual(industry, returned_industry)

    def test_delete_industry_by_id_should_delete_industry_when_it_exists(self):
        industry = IndustryService.create_industry(name='test industry')
        IndustryService.delete_industry_by_id(industry.id)

        try:
            result = IndustryService.get_industry_by_id(industry.id)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_delete_industry_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            IndustryService.delete_industry_by_id(-1)

        self.assertIn('Industry matching query does not exist.', str(context.exception))

    def test_edit_industry_by_id_should_edit_industry(self):
        industry = IndustryService.create_industry(name='test industry')

        IndustryService.edit_industry_by_id(industry.id, name='new test industry')
        changed_industry = IndustryService.get_industry_by_id(industry.id)

        self.assertEqual(industry, changed_industry)
