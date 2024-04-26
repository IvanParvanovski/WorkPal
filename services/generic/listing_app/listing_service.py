from itertools import chain

from django.db.models import Q

from listing_app.models.industry import Industry
from listing_app.models.listing import Listing
from services.interfaces.listing_app.listing_interface import ListingInterface


class ListingService(ListingInterface):
    @staticmethod
    def create_listing(title: str,
                       location: str,
                       description: str,
                       commit=True) -> Listing:

        listing = Listing(
            title=title,
            location=location,
            description=description,
        )

        if commit:
            listing.save()

        return listing

    @staticmethod
    def add_industry_to_listing(listing: Listing, industry: Industry):
        listing.industries.add(industry)

    @staticmethod
    def get_listings_by_industry(industry):
        return Listing.objects.filter(industries=industry)

    @staticmethod
    def search_listings_by_query(query):
        res = []

        for word in query.split():
            res.append(Listing.objects.filter(Q(title__icontains=word) |
                                              Q(industries__name__icontains=word) |
                                              Q(location=word)))

        combined_queryset = chain(*res)
        listings = list(combined_queryset)

        # Create a set to store unique Listing objects
        unique_listings = set()

        # Filter out duplicate Listing objects while preserving order
        for listing in listings:
            if listing not in unique_listings:
                unique_listings.add(listing)

        unique_listings_list = list(unique_listings)

        return unique_listings_list

    @staticmethod
    def get_all_listing_industries(listing):
        return listing.industries.all()

    @staticmethod
    def remove_industry_from_listing(listing: Listing, industry: Industry):
        listing.industries.remove(industry)

    @staticmethod
    def get_all_listings():
        return Listing.objects.all()

    @staticmethod
    def get_listing_by_id(_id: int):
        return Listing.objects.get(id=_id)

    @staticmethod
    def delete_listing(listing):
        listing.delete()

    @staticmethod
    def delete_listing_by_id(_id: int):
        listing = ListingService.get_listing_by_id(_id)
        listing.delete()

    @staticmethod
    def edit_listing_by_id(_id: int,
                           title: str,
                           location: str,
                           description: str,
                           commit=True) -> Listing:

        listing = ListingService.get_listing_by_id(_id)

        listing.title = title
        listing.location = location
        listing.description = description

        if commit:
            listing.save()

        return listing
