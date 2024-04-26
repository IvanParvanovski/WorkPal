from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from services.generic.listing_app.listing_identifiers_service import ListingIdentifiersService
from services.generic.listing_app.listing_service import ListingService


class ListingIdentifiersServiceTestCase(TestCase):
    def setUp(self):
        self.listing = ListingService.create_listing(
            title='test title',
            location='test location',
            description='test description',
        )

    def test_create_listing_identifier_should_add_new_listing_identifier_when_commit_is_not_given(self):
        listing_identifier = ListingIdentifiersService.create_listing_identifier(
            _type='email',
            value='random@gmail.com',
            listing=self.listing
        )

        self.assertEqual('email', listing_identifier.type)
        self.assertEqual('random@gmail.com', listing_identifier.value)
        self.assertEqual(self.listing, listing_identifier.listing)

    def test_create_listing_identifier_should_add_new_listing_identifier_when_commit_is_true(self):
        listing_identifier = ListingIdentifiersService.create_listing_identifier(
            _type='email',
            value='random@gmail.com',
            listing=self.listing,
            commit=True
        )

        created_listing_identifier = ListingIdentifiersService.get_identifier_by_id(_id=listing_identifier.id)

        self.assertEqual('email', created_listing_identifier.type)
        self.assertEqual('random@gmail.com', created_listing_identifier.value)
        self.assertEqual(self.listing, created_listing_identifier.listing)

    def test_create_listing_identifier_should_add_new_listing_identifier_when_commit_is_false(self):
        listing_identifier = ListingIdentifiersService.create_listing_identifier(
            _type='email',
            value='rnadom@gmail.com',
            listing=self.listing,
            commit=False
        )

        try:
            created_object = ListingService.get_listing_by_id(_id=listing_identifier.id)
        except ObjectDoesNotExist:
            created_object = None

        self.assertIsNone(created_object)

    def test_get_identifier_by_id_should_return_identifier_when_it_exists(self):
        listing_identifier = ListingIdentifiersService.create_listing_identifier(
            _type='email',
            value='random@gmail.com',
            listing=self.listing,
        )

        returned_identifier = ListingIdentifiersService.get_identifier_by_id(_id=listing_identifier.id)

        self.assertEqual(listing_identifier, returned_identifier)

    def test_get_identifier_by_id_should_raise_exception_when_id_is_invalid(self):
        try:
            result = ListingIdentifiersService.get_identifier_by_id(-1)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_delete_identifier_should_delete_it_when_it_exists(self):
        listing_identifier = ListingIdentifiersService.create_listing_identifier(
            _type='email',
            value='random@gmail.com',
            listing=self.listing,
        )

        ListingIdentifiersService.delete_identifier(listing_identifier)

        try:
            result = ListingIdentifiersService.get_identifier_by_id(_id=listing_identifier.id)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_delete_identifier_by_id_should_delete_it_when_it_exists(self):
        listing_identifier = ListingIdentifiersService.create_listing_identifier(
            _type='email',
            value='random@gmail.com',
            listing=self.listing,
        )

        ListingIdentifiersService.delete_identifier_by_id(_id=listing_identifier.id)

        try:
            result = ListingIdentifiersService.get_identifier_by_id(_id=listing_identifier.id)
        except ObjectDoesNotExist:
            result = None

        self.assertIsNone(result)

    def test_delete_identifier_by_id_should_raise_exception_when_id_is_invalid(self):
        with self.assertRaises(ObjectDoesNotExist) as context:
            ListingIdentifiersService.delete_identifier_by_id(-1)

        self.assertIn('ListingIdentifiers matching query does not exist.', str(context.exception))

    def test_edit_identifier_should_update_identifier(self):
        listing_identifier = ListingIdentifiersService.create_listing_identifier(
            _type='email',
            value='random@gmail.com',
            listing=self.listing,
        )

        new_listing = ListingService.create_listing(
            title='new test title',
            location='new test location',
            description='new test description'
        )
        new_identifier_data = {
            '_type': 'phone',
            'value': '0898823421',
            'listing': new_listing,
        }

        ListingIdentifiersService.edit_identifier_by_id(_id=listing_identifier.id, **new_identifier_data)
        changed_listing_identifier = ListingIdentifiersService.get_identifier_by_id(_id=listing_identifier.id)

        self.assertEqual(listing_identifier.id, changed_listing_identifier.id)
        self.assertEqual(new_identifier_data['_type'], changed_listing_identifier.type)
        self.assertEqual(new_identifier_data['value'], changed_listing_identifier.value)
        self.assertEqual(new_identifier_data['listing'], changed_listing_identifier.listing)
