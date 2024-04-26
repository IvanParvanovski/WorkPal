from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from services.generic.listing_app.industry_service import IndustryService
from services.generic.listing_app.listing_service import ListingService


class ListingServiceTestCase(TestCase):
    def setUp(self):
        test_listing = {
            'title': 'test listing info',
            'description': 'test description info',
            'location': 'test location info',
        }

        self.test_listing = ListingService.create_listing(test_listing['title'],
                                                          test_listing['description'],
                                                          test_listing['location'])

    def tearDown(self):
        pass

    def test_create_listing_should_add_new_listing_when_commit_is_not_given(self):
        random_listing_info = {
            'title': 'test title',
            'description': 'test description',
            'location': 'test location',
        }

        listing = ListingService.create_listing(**random_listing_info)

        try:
            created_listing = ListingService.get_listing_by_id(_id=listing.id)
        except ObjectDoesNotExist:
            created_listing = None

        self.assertIsNotNone(created_listing)

        self.assertEqual(random_listing_info['title'], created_listing.title)
        self.assertEqual(random_listing_info['description'], created_listing.description)
        self.assertEqual(random_listing_info['location'], created_listing.location)

    def test_create_profile_should_add_new_profile_when_commit_is_true(self):
        random_listing_info = {
            'title': 'test title',
            'description': 'test description',
            'location': 'test location',
        }

        listing = ListingService.create_listing(**random_listing_info, commit=True)

        try:
            created_listing = ListingService.get_listing_by_id(_id=listing.id)
        except ObjectDoesNotExist:
            created_listing = None

        self.assertIsNotNone(created_listing)

        self.assertEqual(random_listing_info['title'], created_listing.title)
        self.assertEqual(random_listing_info['description'], created_listing.description)
        self.assertEqual(random_listing_info['location'], created_listing.location)

    def test_create_profile_should_not_add_profile_when_commit_is_false(self):
        random_listing_info = {
            'title': 'test title',
            'description': 'test description',
            'location': 'test location',
        }

        listing = ListingService.create_listing(**random_listing_info, commit=False)

        try:
            created_listing = ListingService.get_listing_by_id(listing.id)
        except ObjectDoesNotExist:
            created_listing = None

        self.assertIsNone(created_listing)

    def test_add_industry_to_listing_should_add_new_industry(self):
        industry = IndustryService.create_industry(name='test industry')

        ListingService.add_industry_to_listing(listing=self.test_listing, industry=industry)

        self.assertIn(industry, self.test_listing.industries.all())

    def test_get_listing_by_industry_should_return_correct_listings(self):
        test_listing_one_info = {'title': 'random title one',
                                 'description': 'random description one',
                                 'location': 'random location one'}
        test_listing_one = ListingService.create_listing(**test_listing_one_info)

        test_listing_two_info = {'title': 'random title two',
                                 'description': 'random description two',
                                 'location': 'random location two'}
        test_listing_two = ListingService.create_listing(**test_listing_two_info)

        test_listing_three_info = {'title': 'random title three',
                                   'description': 'random description three',
                                   'location': 'random location three'}
        test_listing_three = ListingService.create_listing(**test_listing_three_info)

        test_industry_one = IndustryService.create_industry('test industry one')
        test_industry_two = IndustryService.create_industry('test industry two')

        ListingService.add_industry_to_listing(listing=test_listing_one, industry=test_industry_one)
        ListingService.add_industry_to_listing(listing=test_listing_two, industry=test_industry_one)
        ListingService.add_industry_to_listing(listing=test_listing_three, industry=test_industry_two)

        listings_in_industry_one = ListingService.get_listings_by_industry(industry=test_industry_one)

        self.assertIn(test_listing_one, listings_in_industry_one)
        self.assertIn(test_listing_two, listings_in_industry_one)

    def test_search_listings_by_query_should_return_the_correct_industry(self):
        result = ListingService.search_listings_by_query(query='test')
        self.assertIn(self.test_listing, result)

    def test_get_all_listing_industries_should_return_all_industries_of_a_listing(self):
        industry_one = IndustryService.create_industry('industry one')
        industry_two = IndustryService.create_industry('industry two')
        industry_three = IndustryService.create_industry('industry three')

        ListingService.add_industry_to_listing(listing=self.test_listing, industry=industry_one)
        ListingService.add_industry_to_listing(listing=self.test_listing, industry=industry_two)
        ListingService.add_industry_to_listing(listing=self.test_listing, industry=industry_three)

        industries = ListingService.get_all_listing_industries(listing=self.test_listing)

        self.assertIn(industry_one, industries)
        self.assertIn(industry_two, industries)
        self.assertIn(industry_three, industries)

    def test_remove_industry_from_listing_should_remove_industry_from_the_list(self):
        industry_one = IndustryService.create_industry('industry one')

        ListingService.add_industry_to_listing(listing=self.test_listing, industry=industry_one)
        ListingService.remove_industry_from_listing(listing=self.test_listing, industry=industry_one)

        listing_industries = ListingService.get_all_listing_industries(listing=self.test_listing)
        self.assertNotIn(industry_one, listing_industries)

    def test_get_all_listings_should_return_all_listings(self):
        random_listing = ListingService.create_listing(
            title='random listing',
            description='random description',
            location='random location'
        )

        listings = ListingService.get_all_listings()

        self.assertIn(self.test_listing, listings)
        self.assertIn(random_listing, listings)

    def test_listing_by_id_should_return_correct_listing(self):
        returned_listing = ListingService.get_listing_by_id(_id=self.test_listing.id)
        self.assertEqual(self.test_listing, returned_listing)

    def test_delete_listing_should_delete_the_listing(self):
        ListingService.delete_listing(self.test_listing)

        with self.assertRaises(ObjectDoesNotExist) as context:
            ListingService.get_listing_by_id(self.test_listing.id)

        self.assertEqual('Listing matching query does not exist.', str(context.exception))

    def test_delete_listing_by_id_should_delete_the_listing(self):
        ListingService.delete_listing_by_id(self.test_listing.id)

        with self.assertRaises(ObjectDoesNotExist) as context:
            ListingService.get_listing_by_id(self.test_listing.id)

        self.assertEqual('Listing matching query does not exist.', str(context.exception))

    def test_edit_listing_should_edit_the_listing(self):
        new_info = {
            'title': 'new title',
            'description': 'new description',
            'location': 'new location'
        }

        ListingService.edit_listing_by_id(_id=self.test_listing.id, **new_info)
        changed_listing = ListingService.get_listing_by_id(_id=self.test_listing.id)

        self.assertEqual(new_info['title'], changed_listing.title)
        self.assertEqual(new_info['description'], changed_listing.description)
        self.assertEqual(new_info['location'], changed_listing.location)

