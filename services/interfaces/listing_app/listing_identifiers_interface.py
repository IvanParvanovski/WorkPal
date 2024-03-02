from abc import ABC, abstractmethod

from listing_app.models.listing import Listing
from listing_app.models.listing_identifiers import ListingIdentifiers


class ListingIdentifiersInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_listing_identifier(_type: str,
                                  value,
                                  listing: Listing,
                                  commit=True) -> ListingIdentifiers:
        pass

    @staticmethod
    @abstractmethod
    def get_identifier_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def delete_identifier(identifier: ListingIdentifiers):
        pass

    @staticmethod
    @abstractmethod
    def delete_identifier_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def edit_identifier_by_id(_id: int,
                              _type: str,
                              value,
                              listing: Listing,
                              commit=True) -> ListingIdentifiers:
        pass
