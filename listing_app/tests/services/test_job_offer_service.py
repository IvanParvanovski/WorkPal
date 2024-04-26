from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from services.generic.accounts_app.custom_user_service import CustomUserService
from services.generic.accounts_app.profile_service import ProfileService
from services.generic.company_profiles_app.company_service import CompanyService
from services.generic.listing_app.job_offer_service import JobOfferService
from services.generic.listing_app.listing_service import ListingService


class JobOfferServiceTestCase(TestCase):
    def setUp(self):
        self.listing = ListingService.create_listing(
            title='test title',
            description='test description',
            location='test location'
        )

        self.company = CompanyService.create_company(
            address='test address',
            secondary_address='test secondary address',
            name='test name',
            company_logo='test/logo.png',
            website='https://test.com',
        )

        self.random_job_offer_data = {
            'company': self.company,
            'listing': self.listing,
            'benefits': 'random benefits',
            'salary_range_min': 100,
            'salary_range_max': 101,
            'work_environment': 'test work environment',
            'work_commitment': 'test work commitment',
            'key_responsibilities': 'test key responsibilities',
            'required_qualifications': 'test required qualifications',
            'preferred_qualifications': 'test preferred qualifications',
            'remote_option': True
        }

    def tearDown(self):
        ListingService.delete_listing(self.listing)

    def test_create_job_offer_should_add_new_job_offer_when_commit_is_not_given(self):
        job_offer = JobOfferService.create_job_offer(**self.random_job_offer_data)

        try:
            created_job_offer = JobOfferService.get_job_offer_by_id(job_offer.id)
        except ObjectDoesNotExist:
            created_job_offer = None

        self.assertIsNotNone(created_job_offer)
        self.assertEqual(self.random_job_offer_data['company'],
                         created_job_offer.company)
        self.assertEqual(self.random_job_offer_data['listing'],
                         created_job_offer.listing)
        self.assertEqual(self.random_job_offer_data['benefits'],
                         created_job_offer.benefits)
        self.assertEqual(self.random_job_offer_data['salary_range_min'],
                         created_job_offer.salary_range_min)
        self.assertEqual(self.random_job_offer_data['salary_range_max'],
                         created_job_offer.salary_range_max)
        self.assertEqual(self.random_job_offer_data['work_environment'],
                         created_job_offer.work_environment)
        self.assertEqual(self.random_job_offer_data['work_commitment'],
                         created_job_offer.work_commitment)
        self.assertEqual(self.random_job_offer_data['key_responsibilities'],
                         created_job_offer.key_responsibilities)
        self.assertEqual(self.random_job_offer_data['required_qualifications'],
                         created_job_offer.required_qualifications)
        self.assertEqual(self.random_job_offer_data['preferred_qualifications'],
                         created_job_offer.preferred_qualifications),
        self.assertEqual(self.random_job_offer_data['remote_option'],
                         created_job_offer.remote_option)

    def test_create_job_offer_should_add_new_job_offer_when_commit_is_true(self):
        job_offer = JobOfferService.create_job_offer(**self.random_job_offer_data, commit=True)

        try:
            created_job_offer = JobOfferService.get_job_offer_by_id(job_offer.id)
        except ObjectDoesNotExist:
            created_job_offer = None

        self.assertIsNotNone(created_job_offer)

    def test_create_job_offer_should_add_new_job_offer_when_commit_is_false(self):
        job_offer = JobOfferService.create_job_offer(**self.random_job_offer_data, commit=False)

        try:
            created_job_offer = JobOfferService.get_job_offer_by_id(job_offer.id)
        except ObjectDoesNotExist:
            created_job_offer = None

        self.assertIsNone(created_job_offer)

    def test_get_all_job_offers_should_return_all_job_offers(self):
        for i in range(0, 5):
            current_listing = ListingService.create_listing(
                title='test title',
                description='test description',
                location='test location'
            )

            JobOfferService.create_job_offer(
                company=self.company,
                listing=current_listing,
                benefits=self.random_job_offer_data['benefits'],
                salary_range_min=self.random_job_offer_data['salary_range_min'],
                salary_range_max=self.random_job_offer_data['salary_range_max'],
                work_environment=self.random_job_offer_data['work_environment'],
                work_commitment=self.random_job_offer_data['work_commitment'],
                key_responsibilities=self.random_job_offer_data['key_responsibilities'],
                required_qualifications=self.random_job_offer_data['required_qualifications'],
                preferred_qualifications=self.random_job_offer_data['preferred_qualifications'],
                remote_option=self.random_job_offer_data['remote_option'],
            )

        job_offers = JobOfferService.get_all_job_offers()

        self.assertEqual(5, job_offers.count())

    def test_job_offer_by_id_should_return_job_offer(self):
        job_offer = JobOfferService.create_job_offer(**self.random_job_offer_data)

        returned_job_offer = JobOfferService.get_job_offer_by_id(job_offer.id)

        self.assertEqual(job_offer, returned_job_offer)

    def test_get_job_offer_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            JobOfferService.get_job_offer_by_id(_id=-1)

        self.assertIn('JobOffer matching query does not exist.', str(context.exception))

    def test_get_job_offers_by_company_id_should_return_correct_job_offers(self):
        random_listing_data = {
            'title': 'random title',
            'description': 'random description',
            'location': 'random location'
        }

        listing_one = ListingService.create_listing(**random_listing_data)
        listing_two = ListingService.create_listing(**random_listing_data)

        self.random_job_offer_data['listing'] = listing_one
        job_offer_one = JobOfferService.create_job_offer(**self.random_job_offer_data)

        self.random_job_offer_data['listing'] = listing_two
        job_offer_two = JobOfferService.create_job_offer(**self.random_job_offer_data)

        job_offers = JobOfferService.get_job_offers_by_company_id(self.company.id)

        self.assertIn(job_offer_one, job_offers)
        self.assertIn(job_offer_two, job_offers)

    def test_get_job_offers_by_company_id_should_return_empty_list_when_id_is_invalid(self):
        try:
            result = JobOfferService.get_job_offers_by_company_id(-1)
        except ObjectDoesNotExist:
            result = None

        self.assertEqual(0, result.count())

    def test_get_job_offer_by_listing_id_should_return_correct_job_offers(self):
        job_offer = JobOfferService.create_job_offer(**self.random_job_offer_data)
        returned_job_offer = JobOfferService.get_job_offer_by_listing_id(self.listing.id)
        self.assertEqual(job_offer, returned_job_offer)

    def test_get_job_offer_by_listing_id_should_raise_exception_when_id_is_invalid(self):
        try:
            result = JobOfferService.get_job_offer_by_listing_id(-1)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_delete_job_offer_should_delete_job_offer_when_it_exists(self):
        job_offer = JobOfferService.create_job_offer(**self.random_job_offer_data)

        JobOfferService.delete_job_offer(job_offer)

        try:
            result = JobOfferService.get_job_offer_by_id(job_offer.id)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_delete_job_offer_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            JobOfferService.delete_job_offer_by_id(_id=-1)

        self.assertIn('JobOffer matching query does not exist.', str(context.exception))

    def test_edit_job_offer_should_edit_job_offer(self):
        new_company = CompanyService.create_company(
            address='new test address',
            secondary_address='new test secondary address',
            name='new test name',
            company_logo='new/test/logo.png',
            website='https://test.com',
        )

        new_job_offer_data = {
            'company': new_company,
            'benefits': 'new random benefits',
            'salary_range_min': 1000,
            'salary_range_max': 1001,
            'work_environment': 'new test work environment',
            'work_commitment': 'new test work commitment',
            'key_responsibilities': 'new test key responsibilities',
            'required_qualifications': 'new test required qualifications',
            'preferred_qualifications': 'new test preferred qualifications',
            'remote_option': True
        }

        job_offer = JobOfferService.create_job_offer(**self.random_job_offer_data)
        JobOfferService.edit_job_offer_by_id(job_offer.id, **new_job_offer_data)
        changed_job_offer = JobOfferService.get_job_offer_by_id(job_offer.id)

        self.assertEqual(new_job_offer_data['company'], changed_job_offer.company)
        self.assertEqual(new_job_offer_data['benefits'], changed_job_offer.benefits)
        self.assertEqual(new_job_offer_data['salary_range_min'], changed_job_offer.salary_range_min)
        self.assertEqual(new_job_offer_data['salary_range_max'], changed_job_offer.salary_range_max)
        self.assertEqual(new_job_offer_data['work_environment'], changed_job_offer.work_environment)
        self.assertEqual(new_job_offer_data['work_commitment'], changed_job_offer.work_commitment)
        self.assertEqual(new_job_offer_data['key_responsibilities'], changed_job_offer.key_responsibilities)
        self.assertEqual(new_job_offer_data['required_qualifications'], changed_job_offer.required_qualifications)
        self.assertEqual(new_job_offer_data['preferred_qualifications'], changed_job_offer.preferred_qualifications)
        self.assertEqual(new_job_offer_data['remote_option'], changed_job_offer.remote_option)
