from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from listing_app.models.job_offer import JobOffer
from services.generic.company_profiles_app.company_service import CompanyService
from services.generic.listing_app.job_offer_service import JobOfferService
from services.generic.listing_app.listing_service import ListingService
from services.generic.shared_app.user_suggestion_service import UserSuggestionService


class UserSuggestionServiceTestCase(TestCase):
    def setUp(self):
        self.company = CompanyService.create_company(
            address='test address',
            secondary_address='test secondary address',
            name='test name',
            company_logo='logo/static/image.png',
            website='https://test.com'
        )
        self.listing = ListingService.create_listing(
            title='test title',
            location='test location',
            description='test description'
        )
        self.job_offer = JobOfferService.create_job_offer(
            company=self.company,
            listing=self.listing,
            benefits='test benefit',
            salary_range_min=100,
            salary_range_max=101,
            work_commitment=JobOffer.WorkCommitment.FLEXTIME,
            work_environment=JobOffer.WorkEnvironment.HYBRID,
            key_responsibilities='test key responsibilities',
            required_qualifications='test required qualifications',
            preferred_qualifications='test preferred qualifications',
            remote_option=True
        )

    def test_create_user_suggestion_should_create_user_suggestion_when_commit_is_not_given(self):
        suggestion_data = {
            'field_name': 'work_commitment',
            'suggestion': 'test test',
            'content_type': ContentType.objects.get_for_model(JobOffer),
            'object_id': self.job_offer.id
        }
        suggestion = UserSuggestionService.create_user_suggestion(field_name=suggestion_data['field_name'],
                                                                  suggestion=suggestion_data['suggestion'],
                                                                  content_type=suggestion_data['content_type'],
                                                                  object_id=suggestion_data['object_id'])

        self.assertEqual(suggestion_data['field_name'], suggestion.field_name)
        self.assertEqual(suggestion_data['suggestion'], suggestion.suggestion)
        self.assertEqual(suggestion_data['content_type'], suggestion.content_type)
        self.assertEqual(suggestion_data['object_id'], suggestion.object_id)

    def test_create_user_suggestion_should_create_user_suggestion_when_commit_is_true(self):
        suggestion_data = {
            'field_name': 'work_commitment',
            'suggestion': 'test test',
            'content_type': ContentType.objects.get_for_model(JobOffer),
            'object_id': self.job_offer.id
        }
        suggestion = UserSuggestionService.create_user_suggestion(field_name=suggestion_data['field_name'],
                                                                  suggestion=suggestion_data['suggestion'],
                                                                  content_type=ContentType.objects.get_for_model(
                                                                      JobOffer),
                                                                  object_id=self.job_offer.id,
                                                                  commit=True)

        self.assertEqual(suggestion_data['field_name'], suggestion.field_name)
        self.assertEqual(suggestion_data['suggestion'], suggestion.suggestion)
        self.assertEqual(ContentType.objects.get_for_model(JobOffer), suggestion.content_type)
        self.assertEqual(self.job_offer.id, suggestion.object_id)

    def test_create_user_suggestion_should_create_user_suggestion_when_commit_is_false(self):
        suggestion_data = {
            'field_name': 'work_commitment',
            'suggestion': 'test test'
        }
        suggestion = UserSuggestionService.create_user_suggestion(field_name=suggestion_data['field_name'],
                                                                  suggestion=suggestion_data['suggestion'],
                                                                  content_type=ContentType.objects.get_for_model(
                                                                      JobOffer),
                                                                  object_id=self.job_offer.id,
                                                                  commit=False)

        try:
            created_object = UserSuggestionService.get_user_suggestion_by_id(_id=suggestion.id)
        except ObjectDoesNotExist:
            created_object = None

        self.assertIsNone(created_object)

    def test_get_user_suggestion_by_id_should_return_correct_suggestion(self):
        suggestion_data = {
            'field_name': 'work_commitment',
            'suggestion': 'test test'
        }
        suggestion = UserSuggestionService.create_user_suggestion(field_name=suggestion_data['field_name'],
                                                                  suggestion=suggestion_data['suggestion'],
                                                                  content_type=ContentType.objects.get_for_model(JobOffer),
                                                                  object_id=self.job_offer.id,
                                                                  commit=True)

        returned_object = UserSuggestionService.get_user_suggestion_by_id(_id=suggestion.id)

        self.assertEqual(suggestion, returned_object)

    def test_get_user_suggestion_by_id_should_raise_exception_when_id_is_invalid(self):
        suggestion_data = {
            'field_name': 'work_commitment',
            'suggestion': 'test test'
        }
        suggestion = UserSuggestionService.create_user_suggestion(field_name=suggestion_data['field_name'],
                                                                  suggestion=suggestion_data['suggestion'],
                                                                  content_type=ContentType.objects.get_for_model(
                                                                      JobOffer),
                                                                  object_id=self.job_offer.id,
                                                                  commit=True)

        try:
            returned_object = UserSuggestionService.get_user_suggestion_by_id(_id=-1)
        except ObjectDoesNotExist:
            returned_object = None

        self.assertIsNone(returned_object)

    def test_delete_suggestion_should_delete_suggestion_when_it_exists(self):
        suggestion_data = {
            'field_name': 'work_commitment',
            'suggestion': 'test test'
        }
        suggestion = UserSuggestionService.create_user_suggestion(field_name=suggestion_data['field_name'],
                                                                  suggestion=suggestion_data['suggestion'],
                                                                  content_type=ContentType.objects.get_for_model(
                                                                      JobOffer),
                                                                  object_id=self.job_offer.id,
                                                                  commit=True)

        UserSuggestionService.delete_suggestion(suggestion)

        try:
            returned_object = UserSuggestionService.get_user_suggestion_by_id(_id=suggestion.id)
        except ObjectDoesNotExist:
            returned_object = None

        self.assertIsNone(returned_object)

    def test_delete_user_suggestion_by_id_should_delete_suggestion_when_it_exists(self):
        suggestion_data = {
            'field_name': 'work_commitment',
            'suggestion': 'test test'
        }
        suggestion = UserSuggestionService.create_user_suggestion(field_name=suggestion_data['field_name'],
                                                                  suggestion=suggestion_data['suggestion'],
                                                                  content_type=ContentType.objects.get_for_model(
                                                                      JobOffer),
                                                                  object_id=self.job_offer.id,
                                                                  commit=True)

        UserSuggestionService.delete_suggestion_by_id(suggestion.id)

        try:
            returned_object = UserSuggestionService.get_user_suggestion_by_id(_id=-1)
        except ObjectDoesNotExist:
            returned_object = None

        self.assertIsNone(returned_object)

    def test_edit_user_suggestion_by_id_should_edit_user_suggestion(self):
        suggestion_data = {
            'field_name': 'work_commitment',
            'suggestion': 'test test'
        }

        new_listing = ListingService.create_listing(
            title='new test title',
            location='new test location',
            description='new test description'
        )
        new_job_offer = JobOfferService.create_job_offer(
            company=self.company,
            listing=new_listing,
            benefits='test benefit',
            salary_range_min=100,
            salary_range_max=101,
            work_commitment=JobOffer.WorkCommitment.FLEXTIME,
            work_environment=JobOffer.WorkEnvironment.HYBRID,
            key_responsibilities='test key responsibilities',
            required_qualifications='test required qualifications',
            preferred_qualifications='test preferred qualifications',
            remote_option=True
        )
        new_suggestion_data = {
            'field_name': 'work_environment',
            'suggestion': 'new test test',
            'content_type': ContentType.objects.get_for_model(JobOffer),
            'object_id': new_job_offer.id,
        }

        suggestion = UserSuggestionService.create_user_suggestion(field_name=suggestion_data['field_name'],
                                                                  suggestion=suggestion_data['suggestion'],
                                                                  content_type=ContentType.objects.get_for_model(
                                                                      JobOffer),
                                                                  object_id=self.job_offer.id,
                                                                  commit=True)

        UserSuggestionService.edit_user_suggestion_by_id(_id=suggestion.id,
                                                         field_name=new_suggestion_data['field_name'],
                                                         suggestion=new_suggestion_data['suggestion'],
                                                         content_type=new_suggestion_data['content_type'],
                                                         object_id=new_suggestion_data['object_id'])

        changed_object = UserSuggestionService.get_user_suggestion_by_id(_id=suggestion.id)

        self.assertEqual(new_suggestion_data['field_name'], changed_object.field_name)
        self.assertEqual(new_suggestion_data['suggestion'], changed_object.suggestion)
        self.assertEqual(new_suggestion_data['content_type'], changed_object.content_type)
        self.assertEqual(new_suggestion_data['object_id'], changed_object.object_id)
