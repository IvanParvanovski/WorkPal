from abc import ABC, abstractmethod

from listing_app.models.listing import Listing


class ListingInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_listing(title: str,
                       location: str,
                       images: str,
                       description: str,
                       commit=True) -> Listing:
        pass

    @staticmethod
    @abstractmethod
    def get_all_listings():
        pass

    @staticmethod
    @abstractmethod
    def get_listing_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def delete_listing(listing):
        pass

    @staticmethod
    @abstractmethod
    def delete_listing_by_id(_id: int):
        pass

    @staticmethod
    @abstractmethod
    def edit_listing_by_id(_id: int,
                           title: str,
                           location: str,
                           images: str,
                           description: str,
                           commit=True) -> Listing:
        pass

