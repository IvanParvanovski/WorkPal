from abc import ABC, abstractmethod

from listing_app.models.industry import Industry
from listing_app.models.listing import Listing


class ListingInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_listing(title: str,
                       location: str,
                       description: str,
                       commit=True) -> Listing:
        pass

    @staticmethod
    @abstractmethod
    def add_industry_to_listing(listing: Listing, industry: Industry):
        pass

    @staticmethod
    @abstractmethod
    def get_listings_by_industry(industry):
        pass
    
    @staticmethod
    @abstractmethod
    def get_all_listing_industries(listing):
        pass

    @staticmethod
    @abstractmethod
    def search_listings_by_query(query):
        pass

    @staticmethod
    @abstractmethod
    def remove_industry_from_listing(listing: Listing, industry: Industry):
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
                           description: str,
                           commit=True) -> Listing:
        pass

