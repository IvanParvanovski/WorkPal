from listing_app.models.listing import Listing
from listing_app.models.listing_identifiers import ListingIdentifiers
from services.interfaces.listing_app.listing_identifiers_interface import ListingIdentifiersInterface


class ListingIdentifiersService(ListingIdentifiersInterface):
    @staticmethod
    def create_listing_identifier(_type: str,
                                  value,
                                  listing: Listing) -> ListingIdentifiers:

        identifier = ListingIdentifiers(type=_type, value=value, listing=listing)
        identifier.save()
        return identifier

    @staticmethod
    def get_identifier_by_id(_id: int):
        return ListingIdentifiers.objects.get(id=_id)

    @staticmethod
    def delete_identifier(identifier: ListingIdentifiers):
        identifier.delete()

    @staticmethod
    def delete_identifier_by_id(_id: int):
        identifier = ListingIdentifiersService.get_identifier_by_id(_id=_id)
        identifier.delete()

    @staticmethod
    def edit_identifier_by_id(_id: int,
                              _type: str,
                              value,
                              listing: Listing) -> ListingIdentifiers:

        identifier = ListingIdentifiersService.get_identifier_by_id(_id=_id)

        identifier.type = _type
        identifier.value = value
        identifier.listing = listing

        identifier.save()
        return identifier
